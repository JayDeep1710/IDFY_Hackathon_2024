"use client";
import Header from "../components/Header";
import { Rajdhani } from "next/font/google";
import { useState } from "react";
import Link from "next/link";

const rajdhani = Rajdhani({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

const Select = () => {
  const [bucketName, setBucketName] = useState<string>("");

  return (
    <div className={`${rajdhani.className} flex flex-col min-h-screen`}>
      <main className="flex-grow overflow-hidden bg-[url('/assets/bg.png')] bg-no-repeat bg-cover relative">
        <div className=" inset-0 bg-gradient-to-b from-[rgba(255,0,0,0.3)] to-[rgba(0,0,0,0.3)]"></div>
        <Header header="Local Storage"/>
        <div className="flex flex-col items-center justify-center ">
          <div
            className="p-10"
            style={{ backgroundColor: "rgba(94, 246, 255, 0.25)" }}
          >
            <h1 className="text-[#5EF6FF] text-4xl mb-4">
              ENTER PATH TO LOCAL FOLDER
            </h1>
            <div className="flex flex-col space-y-6">
              <input
                type="text"
                placeholder="Local folder"
                className="p-4 rounded-lg bg-[#224957] text-white text-lg w-full"
                value={bucketName}
                onChange={(e) => setBucketName(e.target.value)}
              />
            
            </div>
          </div>
        </div>
      </main>
      <footer className="p-5 w-full flex justify-between items-center">
        <div className="flex gap-2 items-center">
          <img src="/assets/j.png" alt="intro" className="w-16 h-16" />
          <div>
            <h4 className="text-[#5EF6FF] text-lg">Team - Binary Beasts</h4>
            <h4 className="text-[#5EF6FF] text-lg">Jaydeep</h4>
            <h4 className="text-[#5EF6FF] text-lg">Divy Chokshi</h4>
          </div>
        </div>
        <button
          className="items-center flex px-12 h-16 text-3xl border border-[#5EF6FF] glow-on-hover"
        >
          NEXT
        </button>{" "}
      </footer>
      <img src="assets/footer-line.png" alt="" className="px-5 w-full mb-4" />
    </div>
  );
};

export default Select;
