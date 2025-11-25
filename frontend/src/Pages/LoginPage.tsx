import React from 'react';
import { Link } from 'react-router-dom';
import { useParams } from 'react-router-dom';

import LoginForm from '@/components/LoginForm';
import SigninForm from '@/components/SigninForm';

export const LoginPage = () => {
  const { login_signin } = useParams();
  return (
    <div className="flex flex-col h-screen justify-center items-center">
      {login_signin === 'signin' ? <SigninForm /> : <LoginForm />}
    </div>
  );
};
