import { useEffect, useState } from 'react';

import { toast } from 'sonner';

import api from '@/api';
import { Dock } from '@/components/Dock';
import { FollowingFollowerList } from '@/components/FollowingFollowerList';
import { PostCard } from '@/components/PostCard';
import { UserProfileCard } from '@/components/UserProfileCard';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';

type Post = {
  postid: string;
  username: string;
  profile_pic: string;
  content: string;
  mediaURL: string;
  comments_count: number;
  likes_count: number;
};

export const ProfilePage = () => {
  const [posts, setPosts] = useState<Post[]>([]);

  const fetchPosts = async () => {
    try {
      const response = await api.get('all_posts/');
      const data = response.data;
      setPosts(data);
      console.log(data);
    } catch (error: any) {
      console.log(error);
    }
  };
  const handlePostDelete = async (postid: string) => {
    try {
      await api.delete('post/', {
        params: { postid: postid },
      });
      toast.success('Post Deleted Successfully');
      setPosts((prev) => prev.filter((p) => p.postid !== postid));
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    fetchPosts();
  }, []);

  return (
    <div className="flex flex-col items-center  gap-5">
      <UserProfileCard className="max-w-[800px] w-[90%]" />
      <div className="max-w-[800px] w-[90%] mb-15">
        <Tabs defaultValue="Posts">
          <div className="h-[500px] overflow-y-auto no-scrollbar">
            <TabsList className="bg-background">
              <TabsTrigger value="Posts">Posts</TabsTrigger>
              <TabsTrigger value="Following">Following</TabsTrigger>
              <TabsTrigger value="Follower">Follower</TabsTrigger>
            </TabsList>
            <TabsContent value="Posts" className="animate-in fade-in duration-700 ">
              {posts.length === 0 ? (
                <p className="text-center m-5 text-2xl font-mono">No Post Found, Add Some.</p>
              ) : (
                <>
                  {posts.map((post) => (
                    <PostCard key={post?.postid} post={post} editable onDelete={handlePostDelete} />
                  ))}
                </>
              )}
            </TabsContent>
            <TabsContent value="Following" className="animate-in fade-in duration-700 ">
              <FollowingFollowerList userType="following" />
            </TabsContent>
            <TabsContent value="Follower" className="animate-in fade-in duration-700 ">
              <FollowingFollowerList userType="follower" />
            </TabsContent>
          </div>
        </Tabs>
      </div>
      <Dock />
    </div>
  );
};
