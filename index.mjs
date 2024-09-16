import {chromium} from "playwright";

const port = process.env.BROWSER_PORT || 9001;
const wsPath = process.env.BROWSER_WS_ENDPOINT || "/playwright";


(async () => {
    const server = await chromium.launchServer({host: '0.0.0.0', port, wsPath, headless: false})
    console.log(server.wsEndpoint());
})()