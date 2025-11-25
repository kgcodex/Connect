import { useEffect, useState } from 'react';

import { SquarePen } from 'lucide-react';

import { Input } from '@/components/ui/input';

import { Textarea } from './ui/textarea';

type EditableFieldProps = {
  value: string;
  field: string;
  className?: string;
  textarea?: boolean;
  avatar?: boolean;
  onSubmit: (field: string, value: string | File) => Promise<void>;
};

export const EditableField = ({
  value,
  field,
  onSubmit,
  className,
  textarea,
  avatar,
}: EditableFieldProps) => {
  const [editing, setEditing] = useState(false);
  const [text, setText] = useState(value);

  const handleSubmit = async () => {
    await onSubmit(field, text);
    setEditing(false);
  };

  useEffect(() => {
    setText(value ?? '');
  }, [value]);

  return (
    <>
      {!editing ? (
        <p className={`${className}`}>{value}</p>
      ) : (
        <>
          {avatar ? (
            <Input type="file" accept="image/png, image/jpeg" />
          ) : (
            <>
              {!textarea ? (
                <Input
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
                />
              ) : (
                <Textarea
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  onKeyDown={(e) => e.key === 'Enter' && handleSubmit()}
                />
              )}
            </>
          )}
        </>
      )}
      <SquarePen
        className="invisible group-hover:visible text-gray-300 shrink-0"
        onClick={() => setEditing(true)}
      />
    </>
  );
};
