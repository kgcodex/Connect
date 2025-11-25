import { createBrowserRouter } from 'react-router-dom';

import { HomePage } from './Pages/HomePage';
import { LandingPage } from './Pages/LandingPage';
import { LoginPage } from './Pages/LoginPage';
import { ProfilePage } from './Pages/ProfilePage';
import { SearchPage } from './Pages/SearchPage';

export const router = createBrowserRouter([
  {
    path: '',
    element: <LandingPage />,
  },
  {
    path: 'auth/:login_signin',
    element: <LoginPage />,
  },
  {
    path: 'home',
    element: <HomePage />,
  },
  {
    path: 'search',
    element: <SearchPage />,
  },
  {
    path: 'profile',
    element: <ProfilePage />,
  },
]);
