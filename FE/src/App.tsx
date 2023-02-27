import Loading from 'components/common/loading';
import { useEffect, useState } from 'react';
import Router from 'routes';
import './index.css';

function App() {
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    setLoading(true);
    setTimeout(() => {
      setLoading(false);
    }, 1000);
  }, []);

  return <>{loading ? <Loading /> : <Router />}</>;
}

export default App;
