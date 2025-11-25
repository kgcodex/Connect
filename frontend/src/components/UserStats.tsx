import { useEffect, useState } from 'react';

import { ChartNoAxesColumn } from 'lucide-react';

import api from '@/api';

export const UserStats = () => {
  const [followerCount, setfollowerCount] = useState(0);
  const [followingCount, setfollowingCount] = useState(0);

  const fetchCount = async () => {
    try {
      const response = await api.get('following/', {
        params: { query: 'count' },
      });
      const data = response.data;
      setfollowingCount(data.count);
    } catch (error) {
      console.log(error);
    }
    try {
      const response = await api.get('follower/', {
        params: { query: 'count' },
      });
      const data = response.data;
      setfollowerCount(data.count);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchCount();
  });
  return (
    <div className="flex flex-row justify-end gap-10 items-center">
      {/* Followers  */}
      <div className="flex gap-2 justify-center">
        <ChartNoAxesColumn className="size-15" />
        <div className="flex flex-col  justify-center items-start">
          <p className="text-lg text-gray-300">Following</p>
          <p className="font-mono text-xl">{followingCount}</p>
        </div>
      </div>

      {/* Following  */}
      <div className="flex gap-2 justify-center">
        <ChartNoAxesColumn className="size-15" />
        <div className="flex flex-col  justify-center items-start">
          <p className="text-lg text-gray-300">Followers</p>
          <p className="font-mono text-xl">{followerCount}</p>
        </div>
      </div>
    </div>
  );
};
