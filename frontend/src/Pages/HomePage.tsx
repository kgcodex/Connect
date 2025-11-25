import { Dock } from '@/components/Dock';
import { UserFeed } from '@/components/UserFeed';
import { UserProfileCard } from '@/components/UserProfileCard';

export const HomePage = () => {
  return (
    <>
      <header className="bg-black rounded-b-xl py-2 px-5 mb-5">
        <p className="font-pixelfont text-6xl">C.</p>
      </header>
      <div className="flex flex-row">
        <div className="basis-1/3 p-15 max-lg:hidden">
          <UserProfileCard />
        </div>
        <div className="basis-1/3 max-lg:grow">
          <UserFeed />
        </div>
      </div>
      <Dock />
    </>
  );
};
