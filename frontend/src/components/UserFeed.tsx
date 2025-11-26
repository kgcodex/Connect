import React, { useEffect, useState } from 'react';

import api from '@/api';

import { PostCard } from './PostCard';

type Post = {
  postid: string;
  username: string;
  profile_pic: string;
  content: string;
  mediaURL: string;
  comments_count: number;
  likes_count: number;
};

export const UserFeed = () => {
  const [feed, setFeed] = useState<Post[]>([]);
  const fetchFeed = async () => {
    try {
      const response = await api.get('feed/');
      const data = response.data;
      setFeed(data);
      console.log(data);
    } catch (error: any) {
      console.log(error);
    }
  };
  useEffect(() => {
    fetchFeed();
  }, []);
  return (
    <div className="h-screen border-x-4 border-[#19181a] overflow-auto no-scrollbar space-y-5">
      {feed.length === 0 ? (
        <p className="text-center m-5 text-2xl font-mono">Follow Users to see their posts</p>
      ) : (
        <>
          {feed.map((post) => (
            <PostCard key={post?.postid} post={post} />
          ))}
        </>
      )}
    </div>
  );
};
