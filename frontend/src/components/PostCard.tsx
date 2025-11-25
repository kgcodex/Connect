import { useState } from 'react';

import { Bookmark, Heart } from 'lucide-react';
import { Trash } from 'lucide-react';

import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';

import { Comments } from './Comments';
import { HeartIcon } from './icons/HeartIcon';
import { Skeleton } from './ui/skeleton';

type Post = {
  postid: string;
  username: string;
  profile_pic: string;
  content: string;
  mediaURL: string;
  comments_count: number;
  likes_count: number;
};
type PostCardProps = {
  post: Post;
  editable?: boolean;
  onDelete?: (postid: string) => void;
};

const image_url: string = import.meta.env.VITE_IMAGE_URL;

export const PostCard = ({ post, editable, onDelete }: PostCardProps) => {
  const [loading, setLoading] = useState<Boolean>(true);
  const [like, setLike] = useState<Boolean>(false);

  return (
    <div className="flex flex-col mx-2 p-2 bg-[#19181a] rounded-md mb-4">
      <div className="flex flex-row gap-2 pb-2 items-center justify-between">
        <div className="flex flex-row gap-2 pb-2 items-center">
          <Avatar className="ml-2">
            <AvatarImage
              src={`${image_url}${post?.profile_pic}`}
              alt="User Profile Pic"
            ></AvatarImage>
            <AvatarFallback>{post?.username?.charAt(0).toUpperCase()}</AvatarFallback>
          </Avatar>
          <p className="font-semibold">{post?.username}</p>
        </div>
        {editable && <Trash onClick={() => onDelete?.(post.postid)} />}
      </div>
      <div className="border-0.5 rounded-md flex justify-center items-center bg-background aspect-9/16 h-[400px] overflow-hidden">
        {loading && <Skeleton className="h-full w-full bg-[#272628]" />}
        <img
          className={`object-cover w-full h-full ${loading ? 'hidden' : 'block'}`}
          src={`${image_url}${post?.mediaURL}`}
          alt="Post from the user"
          onLoad={() => setLoading(false)}
        />
      </div>
      <p className="p-2">{post?.content}</p>
      <hr className="bg-black" />
      <div className="flex flex-row items-center justify-around mt-2">
        <div className="flex flex-row gap-2">
          {like ? (
            <div onClick={() => setLike((prev) => !prev)}>
              <HeartIcon />
            </div>
          ) : (
            <Heart onClick={() => setLike((prev) => !prev)} />
          )}
          <p className="text-gray-300">{post?.likes_count}</p>
        </div>
        <div className="flex flex-row gap-2">
          <Comments postid={post?.postid} />
          <p className="text-gray-300">{post?.comments_count}</p>
        </div>
        <Bookmark />
      </div>
    </div>
  );
};
