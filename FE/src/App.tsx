import Loading from 'components/common/loading';
import { useEffect, useState } from 'react';
import { Provider } from 'react-redux';
import Router from 'routes';
import { store } from 'store';
import './index.css';

function App() {
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 1000);
  }, []);

  return (
    <>
      <Provider store={store}>{loading ? <Loading /> : <Router />}</Provider>
    </>
  );
}

export default App;
