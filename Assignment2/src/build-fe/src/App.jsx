import React from "react";
import GlobalStyle from "./globalstyles/globalstyles";
import Home from "./pages/Home";

function App() {
  return (
    <React.Fragment>
      <GlobalStyle />
      <Home />
    </React.Fragment>
  );
}

export default App;
