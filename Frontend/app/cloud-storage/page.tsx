"use client";
import Header from "../components/Header";
import { Rajdhani } from "next/font/google";
import { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import Result from "../result/page";
import { BASE_URL } from "../constant";

const rajdhani = Rajdhani({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
});

const Select = () => {
  const dispatch = useDispatch();
  const [bucketName, setBucketName] = useState<string>("");
  const [accessId, setaccessId] = useState<string>("");
  const [accessKey, setaccessKey] = useState<string>("");
  const [awsRegion, setawsRegion] = useState<string>("");
  const Response = useSelector((state: any) => state);
  const [data, setData] = useState<any | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleCloudApi = () => {
    setIsLoading(true);

    let config = {
      method: "post",
      maxBodyLength: Infinity,
      url: `${BASE_URL}/aws?bucket_name=${bucketName}&aws_access_key_id=${accessId}&aws_secret_access_key=${accessKey}&aws_region=${awsRegion}`,
      headers: {
        accept: "application/json",
      },
    };

    axios
      .request(config)
      .then((response) => {
        setIsLoading(false);
        var res = response.data;
        console.log(response);
        setData(res);
        console.log(Response);
      })
      .catch((error) => {
        console.log(error);
      });
  };

  const goBack = () => {
    window.location.href = "select";
  };

  return (
    <div className={`${rajdhani.className} flex flex-col min-h-screen`}>
      <main className="flex-grow overflow-hidden bg-[url('/assets/bg.png')] bg-no-repeat bg-cover relative">
        <div className=" inset-0 bg-gradient-to-b from-[rgba(255,0,0,0.3)] to-[rgba(0,0,0,0.3)]"></div>
        <Header header="Cloud Storage" />
        {isLoading && (
          <div className="flex justify-center items-center absolute inset-0 mt-40">
            <div className="text-center">
              <div className="spinner mx-auto"></div>
            </div>
          </div>
        )}
        {data === null && !isLoading && (
          <div className="flex flex-col items-center justify-center h-full">
            <div
              className="p-10"
              style={{ backgroundColor: "rgba(94, 246, 255, 0.25)" }}
            >
              <h1 className="text-[#5EF6FF] text-4xl mb-4">
                ENTER THE FOLLOWING DETAILS
              </h1>
              <div className="flex flex-col space-y-6">
                <input
                  type="text"
                  placeholder="Bucket name"
                  className="p-4 rounded-lg bg-[#224957] text-white text-lg w-full"
                  value={bucketName}
                  onChange={(e) => setBucketName(e.target.value)}
                />
                <input
                  type="password"
                  placeholder="AWS Access ID"
                  className="p-4 rounded-lg bg-[#224957] text-white text-lg w-full"
                  value={accessId}
                  onChange={(e) => setaccessId(e.target.value)}
                />
                <input
                  type="password"
                  placeholder="AWS Secret Access Key"
                  className="p-4 rounded-lg bg-[#224957] text-white text-lg w-full"
                  value={accessKey}
                  onChange={(e) => setaccessKey(e.target.value)}
                />
                <input
                  type="text"
                  placeholder="AWS Region"
                  className="p-4 rounded-lg bg-[#224957] text-white text-lg w-full"
                  value={awsRegion}
                  onChange={(e) => setawsRegion(e.target.value)}
                />
              </div>
            </div>
          </div>
        )}
        {data !== null && !isLoading && (
          <Result
            risk_score={data["score"]}
            images={data["images"]}
            code={data["code"]}
            texts={data["texts"]}
          />
        )}
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
          onClick={() => {
            if (data === null) {
              handleCloudApi();
            } else {
              goBack();
            }
          }}
        >
          NEXT
        </button>{" "}
      </footer>
      <img src="assets/footer-line.png" alt="" className="px-5 w-full mb-4" />
    </div>
  );
};

export default Select;
