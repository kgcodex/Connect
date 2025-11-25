import React, { useEffect, useState } from 'react';

import { Plus, X } from 'lucide-react';
import { toast } from 'sonner';

import api from '@/api';
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from '@/components/ui/dialog';

import { Button } from './ui/button';
import { Textarea } from './ui/textarea';

export const CreatePost = () => {
  const [open, setOpen] = useState(false);
  const [preview, setPreview] = useState<string | null>(null);
  const [image, setImage] = useState<File | null>(null);
  const [content, setContent] = useState<string>('');

  const handleImage = (file: File) => {
    setImage(file);
    setPreview(URL.createObjectURL(file));
  };

  const handleDrop = (event: React.DragEvent) => {
    event.preventDefault();
    const file = event.dataTransfer.files?.[0];
    if (file) {
      handleImage(file);
    }
  };

  const handlePost = async () => {
    const payload = new FormData();
    if (content !== '') payload.append('content', content);
    if (image) payload.append('media_url', image);

    if (!image && content.trim() === '') return;

    try {
      await api.post('post/', payload);
      toast.success('Post Created Successfully');
      setTimeout(() => {
        setOpen(false);
      }, 500);
      setPreview(null);
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    setImage(null);
    setPreview(null);
    setContent('');
  }, []);

  return (
    <Dialog open={open} onOpenChange={setOpen}>
      <DialogTrigger asChild>
        <Plus />
      </DialogTrigger>
      <DialogContent>
        <DialogTitle>Create a Post</DialogTitle>
        <DialogHeader>
          <div className="flex flex-col items-center animate-out">
            {preview && (
              <div className="h-[200px] w-full border-2 border-dashed bg-[#141314] rounded-2xl flex justify-center items-center overflow-hidden">
                <img
                  src={preview}
                  alt="Image Preview"
                  className="object-scale-down h-full rounded-xl m-5"
                />
                <X onClick={() => setPreview(null)} />
              </div>
            )}
            {!preview && (
              <div
                className="relative w-full h-full"
                onDragOver={(e) => e.preventDefault()}
                onDrop={(e) => handleDrop(e)}
              >
                <div className="h-[200px] border-2 border-dashed bg-[#141314] rounded-2xl flex justify-center items-center">
                  <p className="text-2xl font-pixelfont text-center text-gray-300">
                    Upload an Image
                  </p>
                </div>
                <input
                  type="file"
                  accept="image/*"
                  className="absolute inset-0 w-full h-full opacity-0 cursor-pointer"
                  onChange={(e) => {
                    e.target.files?.[0] && handleImage(e.target.files?.[0]);
                  }}
                />
              </div>
            )}
            <Textarea
              className="bg-[#141314] mt-5 rounded-2xl p-4 "
              onChange={(e) => setContent(e.target.value)}
            />
          </div>
        </DialogHeader>
        <DialogFooter>
          <DialogClose asChild>
            <Button variant="outline" onClick={() => setPreview(null)}>
              Cancel
            </Button>
          </DialogClose>
          <Button onClick={handlePost} disabled={!image || content.trim() === ''}>
            Post
          </Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  );
};
