import Axios from 'axios';

export const MessageListAdapter = roomId => {
  console.debug(`${roomId} initiated`);
  let incomingHandler = () => {};
  let sendMessageHandler = (msg) => {
    console.debug("sendMessageHandler");
    console.debug(msg);
    Axios.post('http://127.0.0.1:5000/message', {
      post_text: msg
    }).then(function(res) {
      incomingHandler(res.data.result);
    })
  };
  let id;

  return {
    id,
    setIncomingHandler(cb) {
      console.debug("setIncomingHandler");
      incomingHandler = message => {
        //if (message.from !== id)
          cb({
            data: message
            //data: message.data.toString(),
            //peer: message.from
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
