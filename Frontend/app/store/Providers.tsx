// store/Providers.tsx
"use client"; // You must declare this to use hooks or context in the new app directory

import { Provider } from 'react-redux';
import { ReactNode } from 'react';
import { store } from './store';

const Providers = ({ children }: { children: ReactNode }) => {
  return <Provider store={store}>{children}</Provider>;
};

export default Providers;
