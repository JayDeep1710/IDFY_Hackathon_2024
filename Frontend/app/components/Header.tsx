import { Rajdhani } from "next/font/google";
const rajdhani = Rajdhani({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});
const Header = ({header}:{header:string}) => {
  const formatDate = (date: Date): string => {
    const options: Intl.DateTimeFormatOptions = {
      day: 'numeric',
      month: 'long',
      year: 'numeric',
    };
    return date.toLocaleDateString('en-GB', options);
  };
  
  const formatTime = (date: Date): string => {
    const options: Intl.DateTimeFormatOptions = {
      hour: '2-digit',
      minute: '2-digit',
      hour12: true,
    };
    return date.toLocaleTimeString('en-GB', options).toLowerCase();
  };
  const now = new Date();

  return (
    <header className={`${rajdhani.className} p-5 w-full`}>
      <div className={` flex  justify-between`}>
        <div className="flex">
          <img src="/assets/brick.png" alt="intro" className="h-20 mr-2" />
          <div>
            <h1 className="text-3xl text-[#1DED83]">{header}</h1>
            <img
              src="/assets/introduction-line.png"
              alt="intro"
              className="w-40"
            />
            <h6 className="mt-2 text-[#F75049] w-80 text-[10px]">
              This Project was developed for IDFY Fraud Busters hosted on Unstop by the team Binary Beasts.
            </h6>
          </div>
        </div>
        <img src="assets/logo.png" alt="" />
        <div className="flex-col gap-3 items-end">
            <div className="flex gap-2 items-end">
            <h1 className="text-[#F75049] text-2xl font-light">
        {formatDate(now)}
      </h1>
      <h1 className="text-[#1DED83] text-2xl font-light">
        {formatTime(now)}
      </h1>

            </div>
            <img
              src="/assets/loading-bar.png"
              alt="intro"
              className="w-80 mt-4"
            />
        </div>
      </div>
      <img src="assets/header-line.png" alt="" className="w-full mt-4" />
    </header>
  );
};

export default Header;
