import { useForm } from 'react-hook-form';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

import { zodResolver } from '@hookform/resolvers/zod';
import { toast } from 'sonner';
import { z } from 'zod';

import api, { saveTokens } from '@/api.ts';
import { Button } from '@/components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from '@/components/ui/form';
import { Input } from '@/components/ui/input';

// Zod Schema
const loginSchema = z.object({
  email: z.string().email('Enter a valid email'),
  password: z.string().min(8, 'Password must be at least 8 characters'),
});

type loginformtype = z.infer<typeof loginSchema>;

const LoginForm = () => {
  const navigate = useNavigate();
  const form = useForm<loginformtype>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      email: '',
      password: '',
    },
  });

  // Handle Form Submit
  const onSubmit = async (values: loginformtype) => {
    const payload = {
      email: values.email,
      password: values.password,
    };

    try {
      const response = await api.post('login/', payload);
      saveTokens(response.data.access, response.data.refresh);

      toast.success('Welcome');
      navigate('/home');
    } catch (error: any) {
      try {
        const errors = error.response?.data.detail;
        form.setError('email', { message: errors });
      } catch {
        toast.info('Unexpected Error Occur.');
      }
    }
  };

  return (
    <Card className="w-[90%] lg:w-[40%] bg-background">
      <CardHeader>
        <CardTitle className="font-pixelfont text-center font-bold text-6xl">Login</CardTitle>
      </CardHeader>
      <CardContent>
        <Form {...form}>
          <form className="space-y-4 " onSubmit={form.handleSubmit(onSubmit)}>
            {/* User */}
            <FormField
              control={form.control}
              name="email"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Email</FormLabel>
                  <FormControl>
                    <Input type="email" placeholder="Your Email" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            {/* Password  */}
            <FormField
              control={form.control}
              name="password"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Password</FormLabel>
                  <FormControl>
                    <Input type="password" placeholder="Your Password" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            <Button type="submit" className="w-full font-bold text-white lg:mt-5">
              Log in
            </Button>
            <p className="text-center text-gray-500 ">
              Don't have an account.
              <Link to="/auth/signin" className="underline italic">
                Sign in
              </Link>
            </p>
          </form>
        </Form>
      </CardContent>
    </Card>
  );
};

export default LoginForm;
