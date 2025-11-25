import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import { RouterProvider } from 'react-router-dom';

import { Toaster } from '@/components/ui/sonner';

import { ThemeProvider } from './components/theme-provider';
import './index.css';
import { router } from './routes.tsx';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <ThemeProvider defaultTheme="dark" storageKey="theme">
      <RouterProvider router={router} />
      <Toaster />
    </ThemeProvider>
  </StrictMode>
);
