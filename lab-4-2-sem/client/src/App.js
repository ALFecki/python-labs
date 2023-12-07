import Navbar from "./pages/Home"
// import { observer } from 'mobx-react-lite';
import { BrowserRouter } from 'react-router-dom';
// import AppRouter from './components/AppRouter';
// import { useContext, useState, useEffect } from 'react';
// import { Context } from ".";

function App() {
  // const {userStore} = useContext(Context);
  // const [loading, setLoading] = useState(true);


  // useEffect(() => {
  //   setTimeout(() => {
  //     check()
  //       .then(data => {
  //         userStore.setUser(true);
  //         userStore.setIsAuth(true);
  //       })
  //       .catch(e => console.error(e))
  //       .finally(() => setLoading(false));
  //   }, 10)
  // },[])

  // if (loading) {
  //   return <p>Loading...</p>
  // }

  return (
    <BrowserRouter>
      <Navbar />
      {/* <AppRouter /> */}
    </BrowserRouter>
  );
};

export default App;