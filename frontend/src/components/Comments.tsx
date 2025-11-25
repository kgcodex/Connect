import { useState } from 'react';

import { MessageSquare } from 'lucide-react';

import api from '@/api';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Popover, PopoverContent, PopoverTrigger } from '@/components/ui/popover';

import { Input } from './ui/input';

const image_url = import.meta.env.VITE_IMAGE_URL;

type Comments = {
  username: string;
  profile_pic_thumb: string;
  content: string;
};

type CommentsProps = {
  postid: string;
};

export const Comments = ({ postid }: CommentsProps) => {
  const [comments, setComments] = useState<Comments[] | null>(null);

  const fetchComments = async () => {
    try {
      const response = await api.get('comments/', {
        params: { postid: postid },
      });
      setComments(response.data);
    } catch (error: any) {
      if (error.response?.status === 404) {
        setComments([]);
      } else {
        console.log(error);
      }
    }
  };

  const commentOnPost = async (event: React.KeyboardEvent<HTMLInputElement>) => {
    const input = event.currentTarget;
    const content = input.value.trim();
    if (content === '') return;
    await api.post('comments/', {
      post: postid,
      content: content,
    });
    input.value = '';
    fetchComments();
  };

  return (
    <Popover>
      <PopoverTrigger
        asChild
        onClick={() => {
          if (comments === null) fetchComments();
        }}
      >
        <MessageSquare className="cursor-pointer" />
      </PopoverTrigger>
      <PopoverContent className="flex flex-col bg-background w-[500px] h-[500px] border-0">
        <h1 className="text-xl font-mono p-2 ">Comments</h1>
        <hr className="bg-black mb-5" />

        <div className="flex-1 overflow-auto no-scrollbar">
          {comments?.length === 0 ? (
            <p className="text-2xl font-mono text-gray-300 text-center">
              No Comment available for this post.
            </p>
          ) : (
            <>
              {comments?.map((comment) => (
                <div
                  key={comment?.username}
                  className="flex flex-row items-start gap-4 border-b pb-2 mt-2 border-b-gray-500 rounded-bl-xl "
                >
                  <Avatar className="ml-2">
                    <AvatarImage
                      src={`${image_url}${comment?.profile_pic_thumb}`}
                      alt="User Profile Pic"
                    ></AvatarImage>
                    <AvatarFallback>{comment?.username?.charAt(0).toUpperCase()}</AvatarFallback>
                  </Avatar>
                  <div className="flex flex-col items-baseline justify-start">
                    <p className="text-gray-300">{comment?.username}</p>
                    <p className="">{comment?.content}</p>
                  </div>
                </div>
              ))}
            </>
          )}
        </div>
        <div className="mt-4 sticky bottom-0 bg-background">
          <Input
            placeholder="Your Comment"
            onKeyDown={(event) => {
              if (event.key === 'Enter') commentOnPost(event);
            }}
          />
        </div>
      </PopoverContent>
    </Popover>
  );
};
