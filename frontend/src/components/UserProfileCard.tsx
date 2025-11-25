import { useEffect, useState } from 'react';

import { Camera } from 'lucide-react';

import api from '@/api';
import { Avatar, AvatarFallback, AvatarImage } from '@/components/ui/avatar';
import { Card, CardContent } from '@/components/ui/card';

import { EditableField } from './EditableField';
import { UserStats } from './UserStats';

const image_url: string = import.meta.env.VITE_IMAGE_URL;
type User = {
  id: string;
  email: string;
  username: string;
  name: string;
  profile_pic_url: string;
  dob: string;
  bio: string;
};

type CardProp = {
  className?: string;
};

export const UserProfileCard = ({ className }: CardProp) => {
  const [user, setUser] = useState<User>();

  const fetchProfileInfo = async () => {
    try {
      const response = await api.get('profile/');
      const data = response.data;
      console.log(data);
      setUser({
        id: data.id,
        email: data.email,
        username: data.username,
        name: data.name,
        profile_pic_url: data.profile_pic,
        dob: data.dob,
        bio: data.bio,
      });
    } catch (error: any) {
      console.log(error);
    }
  };

  const onSubmit = async (field: string, value: string | File) => {
    const payload = new FormData();
    payload.append(field, value);
    try {
      await api.patch('profile/', payload, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      fetchProfileInfo();
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchProfileInfo();
  }, []);
  return (
    <Card className={`bg-[#141314] mt-10 border-0 h-fit ${className}`}>
      <CardContent>
        <div className="flex flex-row items-center gap-10">
          <div className="group relative size-25">
            {/* Profile Pic */}
            <Avatar className="size-25 absolute">
              <AvatarImage
                src={`${image_url}${user?.profile_pic_url}`}
                alt="User Profile Pic"
              ></AvatarImage>
              <AvatarFallback className="text-2xl bg-background border-4">
                {user?.name?.charAt(0).toUpperCase()}
              </AvatarFallback>
            </Avatar>
            <Camera className=" absolute bottom-0 right-0 invisible group-hover:visible text-gray-300" />
            <input
              type="file"
              placeholder="qwert"
              accept="image/png, image/jpeg "
              className=" size-5 cursor-pointer opacity-0 absolute bottom-0 right-0"
              onChange={(e) => {
                e.target.files?.[0] && onSubmit('profile_pic', e.target.files[0]);
              }}
            />
          </div>
          <div className="flex flex-col gap-2">
            {/* Username */}
            <p className="italic text-gray-300">{`@${user?.username}`}</p>
            <div className="group flex flex-row gap-5 items-center">
              {/* Name  */}
              <EditableField
                value={user?.name ?? ''}
                field="name"
                onSubmit={onSubmit}
                className="text-mono text-2xl"
              />
            </div>
          </div>
        </div>
        {/* Bio  */}
        <div className=" group relative flex flex-row gap-5 items-center">
          <EditableField
            value={user?.bio ?? 'Tell other about yourself'}
            field="bio"
            className="line-clamp-3 mt-2 mr-5"
            onSubmit={onSubmit}
            textarea
          />
        </div>
        <div className="group flex flex-row gap-5 items-center">
          <p className="font-mono mt-2 ">{`DOB: ${user?.dob ?? ''}`}</p>
        </div>
        <UserStats />
      </CardContent>
    </Card>
  );
};
