const Sheets = require("node-sheets").default;
require("dotenv").config();
// dotenv.config();

const gs = new Sheets("1TCnt-KQ3rDDBMHRmyIZkN-5HfLT7zY6m6n2hqQYz6Es");

async function main() {
    await gs.authorizeApiKey(process.env.GOOGLE_SHEET_KEY);
    // await console.log(process.env.GOOGLE_SHEET_KEY)
    // console.log(process.env.GOOGLE_SHEET_KEY)
    const table = await gs.tables("A:F");
    // console.log(table.headers);
    // console.log(table.rows);

}

main()