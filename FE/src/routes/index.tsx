import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Error404 from 'pages/common/error/Error404';
import IndexPage from 'pages/IndexPage';
import PrivateRoute from './PrivateRoute';
import EditListPage from 'pages/listPage';
import MainPage from 'pages/MainPage';
import EditorPage from 'pages/editPage';
import OrderPage from 'pages/orderPage';

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<IndexPage />} path="/" />
        <Route element={<PrivateRoute authentication={false} />}>
          <Route element={<MainPage />} path="/:nansu" />
          <Route element={<EditListPage />} path="/:nansu/list" />
          <Route element={<EditorPage />} path="/:nansu/editor" />
          <Route element={<OrderPage />} path="/:nansu/order" />
        </Route>
        <Route path="/*" element={<Error404 />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;
