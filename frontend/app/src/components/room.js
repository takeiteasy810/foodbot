import React, { Component } from "react";
import {
  Input,
  Button,
} from "react-chat-elements";

import MessageList from "./MessageList";
import MessageListAdapter from "./messageListAdapter";

export class Room extends Component {
  constructor(props) {
    super(props);
    this.messageListAdapter = new MessageListAdapter("roomNo");
    this.state = {
      meId: this.messageListAdapter.id,
      show: true,
      messageList: []
    };
  }

  componentDidMount() {
    // はじめの一文
    this.addMessage("今日は何たべる？", {
      position: "left",
      theme: "gray"
    });
    // 返信を表示
    this.messageListAdapter.setIncomingHandler(msg => {
      console.log(msg.data)
      if (msg.data.error) { // Errorがある場合
        this.addMessage(msg.data.error, {
          position: "left",
          theme: "gray",
        });
      } else { // 正常の場合
        this.addMessage(
          'こちらのお店はいかがですか？', {
          position: "left",
          theme: "gray",
        });
        // 本題
        this.addMessage(
          '<img style="width:200px" src="' + msg.data.image + '" /><h2>' + msg.data.shopName + '</h2><a>' + msg.data.catch + '</a><br><a>' + msg.data.open + '</a><br><a href="' + msg.data.url + '" target="_blank">→お店の詳細はこちら</a>'
          , {
            position: "left",
            theme: "gray",
          });
      }
    });
  }

  // メッセージ表示のデザインテンプレート
  addMessage(msg, opts) {
    console.debug("addMessage");
    var list = this.state.messageList;
    list.push(
      Object.assign(
        {
          position: "right",
          type: "text",
          theme: "black",
          view: "list",
          text: msg,
          date: new Date(),
          dateString: " ",
          notch: true,
          focus: true
        },
        opts
      )
    );
    this.setState({
      messageList: list
    });
  }

  // 入力した文字を送信
  async sendMessage() {
    if (this.refs.input.input.value.length > 0) {
      // 入力したメッセージを吹き出し表示
      this.addMessage(this.refs.input.input.value);
      // 位置情報取得・セット
      navigator.geolocation.getCurrentPosition(position => {
        // メッセージをAPIに送信
        this.messageListAdapter.sendMessage({
          // 入力した文字
          inputMessage: this.refs.input.input.value,
          // 入力者の位置情報
          gpsValue: {
            latitude: position.coords.latitude,
            longitude: position.coords.longitude
          }
        });
        // テキストボックスから入力した文字を削除
        this.refs.input.clear();
      })
    }
  }

  render() {
    console.debug("render");
    return (
      <div className="right-panel">
        <MessageList
          className="message-list"
          lockable={false}
          downButton={true}
          dataSource={this.state.messageList}
        />
        <Input
          placeholder="めっせーじを入力..."
          defaultValue=""
          ref="input"
          multiline={true}
          // buttonsFloat='left'
          onKeyPress={e => {
            if (e.shiftKey && e.charCode === 13) {
              return true;
            }
            if (e.charCode === 13 && this.refs.input.input.value.length > 0) {
              this.sendMessage();
              e.preventDefault();
              return false;
            }
          }}
          rightButtons={
            <Button text="送信" onClick={this.sendMessage.bind(this)} />
          }
        />
      </div>
    );
  }
}

export default Room;

