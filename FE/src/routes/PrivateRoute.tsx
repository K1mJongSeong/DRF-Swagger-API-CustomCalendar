import { useAppDispatch } from 'hooks';
import { ReactElement, useEffect } from 'react';
import { Navigate, Outlet, useParams } from 'react-router-dom';
import { getVerifyNansu } from 'reducer/auth';

interface PrivateRouteProps {
  children?: ReactElement; // Router.tsx에서 PrivateRoute가 감싸고 있는 Componet Element
  authentication: boolean; // true :인증을 반드시 해야하만 접속가능, false : 인증을 반디스 안해야만 접속 가능
}

export default function PrivateRoute({
  authentication,
}: PrivateRouteProps): React.ReactElement | null {
  const dispatch = useAppDispatch();
  const params = useParams();
  const { nansu } = params;

  const isAuthenticated = sessionStorage.getItem('isAuthenticated');

  useEffect(() => {
    dispatch(getVerifyNansu(nansu as string));
  }, []);

  if (authentication) {
    // 인증이 반드시 필요한 페이지
    return isAuthenticated === null || isAuthenticated === 'false' ? (
      <Navigate to="/" />
    ) : (
      <Outlet />
    );
  } else {
    // 인증이 반드시 필요 없는 페이지
    return isAuthenticated === null || isAuthenticated === 'false' ? (
      <Outlet />
    ) : (
      <Navigate to="/" />
    );
  }
}
