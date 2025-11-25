import { useEffect, useState } from 'react';

import api from '@/api';

import { UserBar } from './UserBar';

type FollowingFollowerListProps = {
  userType: 'following' | 'follower';
};

type UserList = {
  id: string;
  username: string;
  profile_pic_thumb: string;
};

export const FollowingFollowerList = ({ userType }: FollowingFollowerListProps) => {
  const [users, setUsers] = useState<UserList[]>([]);
  const [loading, setLoading] = useState(true);

  const fetchUsers = async () => {
    if (userType === 'following') {
      try {
        const response = await api.get('following/', {
          params: { query: 'list' },
        });
        const data = response.data;
        setUsers(data);
        setLoading(false);
      } catch (error) {
        console.log(error);
      }
    } else {
      try {
        const response = await api.get('follower/', {
          params: { query: 'list' },
        });

        const data = response.data;
        setUsers(data);
        setLoading(false);
      } catch (error) {
        console.log(error);
      }
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);
  return (
    <>
      {loading ? (
        <p className="text-center m-5 text-2xl font-mono">Loading</p>
      ) : (
        <>
          {users.length === 0 ? (
            <p className="text-center m-5 text-2xl font-mono">No User Found</p>
          ) : (
            users.map((user) => (
              <UserBar
                key={user.username}
                className="w-full"
                username={user.username}
                profile_pic_thumb={user.profile_pic_thumb}
                showFollowButton={userType === 'follower'}
              />
            ))
          )}
        </>
      )}
    </>
  );
};
