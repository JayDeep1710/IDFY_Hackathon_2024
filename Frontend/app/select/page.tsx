"use client";
import Header from "../components/Header";
import { Rajdhani } from "next/font/google";
import { useState } from 'react';

const rajdhani = Rajdhani({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

const data=['CLOUD STORAGE','SQL DATA','LOCAL FOLDER','OTHER'];
const links=['/cloud-storage','sql','/local-folder','/other'];
const Select = () => {
  
  return (
    <div className={`${rajdhani.className} flex flex-col min-h-screen`}>
      <main className="flex-grow  overflow-hidden bg-[url('/assets/bg.png')] bg-no-repeat bg-cover relative">
        <div className=" inset-0 bg-gradient-to-b from-red-500 to-black opacity-30"></div>
        <Header header="Select the data"/>
        <div className="flex flex-col items-center justify-center h-full">
          <h1
            className="relative z-10 text-6xl text-center text-[#F75049] w-[60%]
              [text-shadow:0_0_10px_#F75049,0_0_20px_#F75049,0_0_30px_#F75049]"
          >
            Select your data
          </h1>
          {Array.from({ length: 4 }, (_, index) => (
            <button onClick={()=>window.location.href=links[index]} className="w-[40%] my-4 px-12 h-16 text-3xl border border-[#5EF6FF] transform transition-all duration-2000 ease-in-out hover:scale-101 glow-on-hover2">
            {data[index]}
          </button>
          
          ))}
        </div>
      </main>
    </div>
  );
};

export default Select;
