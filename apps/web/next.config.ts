import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  experimental: {
    turbo: {
      root: "/Users/macbookpro/Desktop/Portal",
    },
  },
  transpilePackages: ["@tsz-portal/database"],
};

export default nextConfig;