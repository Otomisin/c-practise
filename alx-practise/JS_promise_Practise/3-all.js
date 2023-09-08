import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const photo = uploadPhoto();
  const user = createUser();

  return Promise.all([photo, user])
    .then((values) => {
      const profile = values[0].body;
      const first = values[1].firstName;
      const last = values[1].lastName;

      console.log(
        `${profile} ${first} ${last}`,
      );
    })
    .catch(() => console.log('Signup system offline'));
}
