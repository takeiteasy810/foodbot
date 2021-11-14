import React from "react";
import ReactDOM from "react-dom";
import Room from "./components/room";
// import List from "./components/list";
import "react-chat-elements/dist/main.css";
import "./styles.css";

function App() {
  return (
    <div className="App">
      <div className="container">
        <Room />
      </div>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
