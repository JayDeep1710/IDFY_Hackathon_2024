import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import Providers from "./store/Providers";


export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <Providers>
          {children}
        </Providers>
      </body>
    </html>
  );
}
