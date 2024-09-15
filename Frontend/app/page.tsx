import Header from "./components/Header";
import { Rajdhani } from "next/font/google";
import NextButton from "./components/next-button";

const rajdhani = Rajdhani({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

export default function Home() {
  return (
    <div className={`${rajdhani.className} flex flex-col min-h-screen`}>
      <main className="flex-grow  overflow-hidden bg-[url('/assets/bg.png')] bg-no-repeat bg-cover relative">
        <div className=" inset-0 bg-gradient-to-b from-red-500 to-black opacity-30"></div>
        <Header header="Introduction"/>
        <div className="flex flex-col items-center justify-center">
          <h1
            className="relative z-10 text-8xl text-center text-[#F75049] w-[60%]
              [text-shadow:0_0_10px_#F75049,0_0_20px_#F75049,0_0_30px_#F75049]
              [animation:flicker_3s_6_forwards]"
          >
            PRIVACY SHERLOCK EFFICIENTLY UNCOVER SENSITIVE DATA
          </h1>
          <p className="mt-4 relative z-10 text-lg text-center text-[#1DED83] w-[60%]">
            DISCOVER WAYS TO DETECT PERSONALLY IDENTIFIABLE INFORMATION (PII)
            WITHIN DIVERSE DATA REPOSITORIES, INCLUDING RELATIONAL DATABASES,
            CLOUD STORAGE SERVICES AND FILE SYSTEMS. THIS TOOL WILL ACCURATELY
            DETERMINE THE PRESENCE AND TYPE OF PII IN EACH DATA POINT AND
            SUBSEQUENTLY ASSESS THE ASSOCIATED RISK LEVEL FOR THE ENTIRE
            DATABASE OR OBJECT.
          </p>
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
        <NextButton/>
      </footer>
      <img src="assets/footer-line.png" alt="" className="px-5 w-full mb-4" />
    </div>
  );
}
