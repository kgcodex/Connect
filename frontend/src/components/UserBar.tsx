import { useState } from 'react';

import { toast } from 'sonner';

import api from '@/api';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Button } from '@/components/ui/button';

const image_url: string = import.meta.env.VITE_IMAGE_URL;
type UserBarProp = {
  profile_pic_thumb: string;
  username: string;
  showFollowButton: boolean;
  className?: string;
};
export const UserBar = ({
  profile_pic_thumb,
  username,
  showFollowButton,
  className,
}: UserBarProp) => {
  const [disableFollow, setDisableFollow] = useState(false);
  const handleFollow = async () => {
    const payload = {
      username: username,
    };
    try {
      await api.post('following/', payload);
      toast.success(`You are now following ${username}`);
      setDisableFollow(true);
    } catch (errors: any) {
      if (errors.response?.status === 400) {
        toast.info(`You already follow ${username}`);
        setDisableFollow(true);
      }
      console.log(errors);
    }
  };
  return (
    <div
      className={`flex items-center justify-between bg-[#141314] max-w-[800px] w-[90%] mb-5 h-10 p-10 rounded-xl ${className}`}
    >
      <div className="flex items-center gap-4">
        <Avatar className="size-10">
          <AvatarImage
            src={`${image_url}${profile_pic_thumb}`}
            alt="User Profile Pic"
          ></AvatarImage>
          <AvatarFallback className="text-2xl bg-background border-4">
            {username?.charAt(0).toUpperCase()}
          </AvatarFallback>
        </Avatar>
        <h1 className="text-2xl font-semibold font-mono">{username}</h1>
      </div>
      {showFollowButton && (
        <Button
          className="text-semibold text-white"
          onClick={handleFollow}
          disabled={disableFollow}
        >
          Follow
        </Button>
      )}
    </div>
  );
};
