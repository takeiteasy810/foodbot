import Axios from 'axios';

export const MessageListAdapter = roomId => {
  console.debug(`${roomId} initiated`);
  let incomingHandler = () => { };


  let sendMessageHandler = (msg) => {
    // JSON形式で送る
    Axios.post('http://127.0.0.1:5000/message', {
      post_text: msg.inputMessage,
      gps_Value: msg.gpsValue
    }).then(function (res) {
      incomingHandler(res.data);
    })
  };


  let id;
  return {
    id,
    setIncomingHandler(cb) {
      console.debug("setIncomingHandler");
      incomingHandler = message => {
        cb({
          data: message
        });
      };
    },
    sendMessage(msg) {
      console.debug("sendMessage");
      sendMessageHandler(msg);
    }
  };
};

export default MessageListAdapter;
