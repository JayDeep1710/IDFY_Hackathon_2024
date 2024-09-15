"use client";
import Header from "../components/Header";
import { Rajdhani } from "next/font/google";
import { useState,useEffect } from "react";
import { useSelector } from "react-redux";

const rajdhani = Rajdhani({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});


const Result = ({risk_score,texts,images,code}:{risk_score:number,texts:any,images:any,code:any}) => {
  
  return (
    <div className={`${rajdhani.className}`}>
  <div className="flex items-center justify-center">
    <div className="flex flex-col">
      {/* Risk Score Section */}
      <div className="flex items-center justify-center mb-8 bg-[#181818] p-4 border-[#5EF6FF] border">
        <div className="relative w-32 h-32 rounded-full border-8 border-gray-500 flex items-center justify-center">
          <span className="text-4xl font-bold">{risk_score}</span>
          <span className="absolute bottom-2 text-sm text-gray-300">
            Risk Score
          </span>
        </div>
      </div>

      {/* Images Section */}
      <div className="flex flex-col text-[#1DED83] items-center justify-start mb-8 bg-[#181818] p-4 border-[#5EF6FF] border h-[200px] w-[300px] overflow-y-auto">
  <h1 className="text-xl mb-3">Images</h1>
  <ul className="w-full">
    {Object.entries(images).map(([key, value]) => (
      <li key={key} className="flex justify-between w-full mb-2">
        <span className="font-bold uppercase">{key}</span>
        <span className="opacity-80">{String(value)}</span>
      </li>
    ))}
  </ul>
</div>

    </div>

    {/* Scrollable Box for Right Side */}
    <div className="ml-5 flex flex-col items-center justify-start mb-8 bg-[#181818] p-4 border-[#5EF6FF] border h-[400px] w-2/5 overflow-y-auto">
      
    <h1 className="text-xl mb-3">Texts</h1>

  <ul className="w-full">
    {Object.entries(texts).map(([fileName, fileContent]: [any, any]) => {
      // Ignore empty maps
      if (Object.keys(fileContent).length === 0) return null;

      return (
        <li key={fileName} className="mb-4">
          {/* File Name */}
          <div className="font-bold uppercase text-[#1DED83] mb-2">
            {fileName}
          </div>
          <ul className="w-full">
            {/* Map over the content of each file */}
            {Object.entries(fileContent).map(([key, value]: [any, any]) => (
              <li key={key} className="flex justify-between w-full">
                <span className="font-bold uppercase">{value}</span>
                <span className="opacity-80">{String(key)}</span>
              </li>
            ))}
          </ul>
        </li>
      );
    })}
  </ul>
</div>

  </div>
</div>


  );
};

export default Result;
