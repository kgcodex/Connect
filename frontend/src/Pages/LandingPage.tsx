import React from 'react';
import { Link, Links } from 'react-router-dom';

import landingimage from '@/assets/landingimage.svg';
import { Button } from '@/components/ui/button.tsx';

export const LandingPage = () => {
  return (
    <>
      <nav className=" px-5 shadow-primary shadow-2xl rounded-2xl my-5 mx-5">
        <div className="flex flex-row justify-between items-center">
          <p className="font-pixelfont text-7xl">C.</p>
          <div className="flex gap-4">
            <Button className="font-semibold text-white">Home</Button>
            <Button className="font-semibold text-white">About</Button>
          </div>
        </div>
      </nav>

      <main>
        <div className="flex flex-col lg:flex-row lg:gap-40 ">
          <div>
            <h1 className="font-pixelfont text-8xl text-center mt-10 md:text-10xl lg:text-[200px] lg:text-left lg:ml-15">
              Connect.
            </h1>
            <p className="font-mono text-center text-2xl mx-5 mt-2 lg:text-[50px] lg:ml-15 lg:text-left">
              Lets connect to the world..
            </p>
            <div className="flex gap-10 justify-center mt-10 mb-5 lg:justify-start lg:ml-30">
              <Link to="/auth/login">
                <Button className="text-xl font-bold text-white" size="lg">
                  Log in
                </Button>
              </Link>
              <Link to="/auth/signin">
                <Button className="text-xl font-bold text-white" size="lg">
                  Sign in
                </Button>
              </Link>
            </div>
          </div>

          <img
            src={landingimage}
            alt="landing image"
            className="size-2xl lg:size-150 rounded-t-[40%] lg:rounded-2xl lg:mt-20"
          />
        </div>
      </main>
    </>
  );
};
