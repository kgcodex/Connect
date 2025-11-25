import { useForm } from 'react-hook-form';
import { Link } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';

import { zodResolver } from '@hookform/resolvers/zod';
import { toast } from 'sonner';
import { z } from 'zod';

import api from '@/api.ts';
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
const signinSchema = z
  .object({
    name: z.string(),
    username: z.string(),
    email: z.string().email('Enter a valid email'),
    dob: z.string().refine((val) => {
      const date = new Date(val);
      if (isNaN(date.getTime())) return false; //Date is valid or not

      const today = new Date();
      let age = today.getFullYear() - date.getFullYear();
      const monthdiff = today.getMonth() - date.getMonth();
      if (monthdiff < 0 || (monthdiff === 0 && today.getDate() < date.getDate())) {
        age--;
      }
      return age >= 18;
    }, 'Age must be 18 or above'),
    password: z.string().min(8, 'Password must be at least 8 characters'),
    confirmPassword: z.string(),
  })
  .refine((data) => data.password === data.confirmPassword, {
    message: 'Password does not match',
    path: ['confirmPassword'],
  });

type signinformtype = z.infer<typeof signinSchema>;

const SigninForm = () => {
  const navigate = useNavigate();

  const form = useForm<signinformtype>({
    resolver: zodResolver(signinSchema),
    defaultValues: {
      name: '',
      username: '',
      email: '',
      dob: '',
      password: '',
      confirmPassword: '',
    },
  });

  // Handle Form Submit
  const onSubmit = async (values: signinformtype) => {
    const payload = {
      name: values.name,
      username: values.username,
      email: values.email,
      dob: values.dob,
      password: values.password,
    };

    try {
      await api.post('register/', payload);
      toast.success('Account created successfully.');

      navigate('/auth/login');
    } catch (error: any) {
      try {
        const errors = error.response?.data;

        if (errors?.email) {
          form.setError('email', { message: errors.email[0] });
        }

        if (errors?.username) {
          form.setError('username', { message: errors.username[0] });
        }
      } catch {
        toast.info('Unexpected Error Occur.');
      }
    }
  };

  return (
    <Card className="w-[90%] lg:w-[40%] bg-background">
      <CardHeader>
        <CardTitle className="font-pixelfont text-center text-6xl">Connect.</CardTitle>
      </CardHeader>
      <CardContent>
        <Form {...form}>
          <form className="space-y-4 " onSubmit={form.handleSubmit(onSubmit)}>
            {/* Name */}
            <FormField
              control={form.control}
              name="name"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Name</FormLabel>
                  <FormControl>
                    <Input placeholder="Your Name" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            {/* Username  */}
            <FormField
              control={form.control}
              name="username"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Username</FormLabel>
                  <FormControl>
                    <Input placeholder="Username" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            {/* Email  */}
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

            {/* DOB  */}
            <FormField
              control={form.control}
              name="dob"
              render={({ field }) => (
                <FormItem>
                  <FormLabel>Date of Birth</FormLabel>
                  <FormControl>
                    <Input type="date" placeholder="Date of Birth" {...field} />
                  </FormControl>
                  <FormMessage />
                </FormItem>
              )}
            />

            <div className="lg:flex lg:flex-row lg:gap-5 lg:items-center max-lg:space-y-4">
              {/* Password  */}
              <div className="lg:w-1/2">
                <FormField
                  control={form.control}
                  name="password"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Password</FormLabel>
                      <FormControl>
                        <Input type="password" placeholder="User Secure Password" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
              </div>

              {/* Confirm Password  */}
              <div className="lg:w-1/2">
                <FormField
                  control={form.control}
                  name="confirmPassword"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Confirm Password</FormLabel>
                      <FormControl>
                        <Input placeholder="Renter Password" {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
              </div>
            </div>

            <Button type="submit" className="w-full font-bold text-white lg:mt-5">
              Sign in
            </Button>
          </form>
        </Form>
        <p className="text-center text-gray-500 mt-2">
          Already have a account.
          <Link to="/auth/login" className="underline italic">
            Log in
          </Link>
        </p>
      </CardContent>
    </Card>
  );
};

export default SigninForm;
