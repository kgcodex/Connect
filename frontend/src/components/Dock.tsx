import { Link } from 'react-router-dom';

import { House, Search, User } from 'lucide-react';

import { CreatePost } from './CreatePost';

export const Dock = () => {
  return (
    <div className="fixed bottom-0 left-1/2 -translate-x-1/2 w-[90%] max-w-[400px] h-[50px] mb-5 bg-black flex items-center justify-around rounded-xl shadow-xl opacity-0 hover:opacity-100">
      <Link
        to="/home"
        className="hover:bg-[#141314] size-12 flex items-center justify-center rounded-full border-0"
      >
        <House />
      </Link>

      <div className="hover:bg-[#141314] size-12 flex items-center justify-center rounded-full border-0 ">
        <CreatePost />
      </div>

      <Link
        to="/search"
        className="hover:bg-[#141314] size-12 flex items-center justify-center rounded-full border-0"
      >
        <Search />
      </Link>

      <Link
        to="/profile"
        className="hover:bg-[#141314] size-12 flex items-center justify-center rounded-full border-0"
      >
        <User />
      </Link>
    </div>
  );
};
