# SQL Scratchpad

Install and open:

    npm install
    firefox index.html

Concept:

We have the `gethue` dependency in `packages.json` or run `npm install gethue`. Then just load it similarly to:

    import sqlScratchpadComp from 'gethue/lib/components/SqlScratchpadWebComponent';

    window.onload = async function (){
      sqlScratchpadComp.setBaseUrl('http://locahost:9000');
      await sqlScratchpadComp.login('hue', 'hue');
    |

In HTML:

    <sql-scratchpad dialect="mysql" />

API:

Can be running Compose server or Hue on http://locahost:9000.
