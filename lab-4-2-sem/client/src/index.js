import './styles/index.css';
import App from './App';
import ReactDOM from 'react-dom/client';
import React, { createContext } from 'react';
// import UserStore from './store/UserStore';

export const Context = createContext(null);


const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    {/* <Context.Provider value={{
      // userStore: new UserStore(),
      // cardStore: new CardStore(),
      // adminStore: new AdminStore(),
    }}> */}

      <App />
    {/* </Context.Provider> */}
  </React.StrictMode>
);

