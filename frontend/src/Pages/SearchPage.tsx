import React, { useState } from 'react';

import { Search } from 'lucide-react';

import api from '@/api';
import { Dock } from '@/components/Dock';
import { UserBar } from '@/components/UserBar';
import { Input } from '@/components/ui/input';

type SearchResult = {
  id: string;
  username: string;
  profile_pic_thumb: string;
};

export const SearchPage = () => {
  const [searchResult, setSearchResult] = useState<SearchResult[] | null>(null);

  const searchUser = async (event: React.KeyboardEvent<HTMLInputElement>) => {
    const input = event.currentTarget;
    const username = input.value.trim();
    try {
      const response = await api.get('search/', {
        params: { username: username },
      });
      setSearchResult(response.data);
    } catch (error: any) {
      if (error.response?.status === 404) {
        setSearchResult([]);
      } else {
        console.log(error);
      }
    }
  };
  return (
    <>
      <header className="bg-black rounded-b-xl py-2 px-5 mb-5">
        <p className="font-pixelfont text-6xl">C.</p>
      </header>
      <div className="flex flex-col items-center">
        <div className="w-[90%] max-w-[800px]">
          <div className="flex items-center justify-center gap-2 w-[90%] max-w-[800px]">
            <Search />
            <Input
              placeholder="Search for user through username"
              onKeyDown={(event) => {
                if (event.key === 'Enter') searchUser(event);
              }}
            />
          </div>
          <p className="text-left text-2xl mt-5 mb-2">Users</p>
          <hr className="bg-black mb-5" />
        </div>

        {searchResult === null ? (
          <></>
        ) : searchResult.length === 0 ? (
          <p className="text-center m-5 text-2xl font-mono">No User Found with this username</p>
        ) : (
          searchResult.map((user) => (
            <UserBar
              key={user?.username}
              profile_pic_thumb={user?.profile_pic_thumb}
              username={user?.username}
              showFollowButton
            />
          ))
        )}
      </div>
      <Dock />
    </>
  );
};
