import React, { Component } from "react";
import {
  Input,
  Button,
} from "react-chat-elements";

import MessageList from "./MessageList";

import Identicon from "identicon.js";
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
    console.debug("componentDidMount");
    this.addMessage("今日は何たべる？", {
      position: "left",
      theme: "gray"
    });
    this.messageListAdapter.setIncomingHandler(msg => {
      this.addMessage(msg.data, {
        position: "left",
        theme: "gray",
        //avatar: this.photo(42, msg.peer)
      });
    });
  }
  token() {
    console.debug("token");
    return parseInt((Math.random() * 10) % 6);
  }
  photo(size, peer) {
    console.debug("photo");
    const data = new Identicon(peer.substr(-15), {
      size,
      margin: 0.2,
      format: "svg"
    });
    return `data:image/svg+xml;base64,${data}`;
  }
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

  sendMessage() {
    if (this.refs.input.input.value.length > 0){
      this.addMessage(this.refs.input.input.value);
      this.messageListAdapter.sendMessage(this.refs.input.input.value);
      this.refs.input.clear();
    }
    // グルメサーチAPIの結果を取得して成形して表示したい
    this.addMessage('こちらのお店はいかがですか？',{position: "left",theme: "gray",});
    this.addMessage('<div style="width:200px; height:200px; border:1px solid #DFDFDF; text-align:center;"><img style="width:200px" src="https://imgfp.hotp.jp/IMGH/64/29/P037716429/P037716429_480.jpg" /></div><br/><span style="font-weight:bold; font-size:18px">フレンチバル　レサンス</span><br/><span>【ネット予約可】フレンチバル レサンス（イタリアン・フレンチ/フレンチ）の予約なら、お得なクーポン満載、24時間ネット予約でポイントもたまる【ホットペッパーグルメ】！おすすめはご自宅や仕事場でもお楽しみいただけます。バルのアラカルトメニューからお選びください。 誕生日や記念日など、特別な1日のお食事にはプレートをご用意♪クーポンの利用でサービス可能です★※この店舗はネット予約に対応しています。</span><br/><a href="https://www.hotpepper.jp/strJ001197579/" target="_blank">→ご予約はこちら</a>', {
      position: "left",
      theme: "gray",
    });
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

