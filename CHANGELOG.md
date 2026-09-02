# Changelog

## 1.0.0 (2026-09-02)


### 🚀 Features

* initialize project with core configuration and documentation ([fff7ffd](https://github.com/nlamirault/kortex/commit/fff7ffdb57aa0a75808f0cecdbd2ba9a34ddddb0))
* **website:** deploy wiki to Cloudflare Workers ([#15](https://github.com/nlamirault/kortex/issues/15)) ([b6dc76a](https://github.com/nlamirault/kortex/commit/b6dc76a9c4c4e0ec58fe6df9d4b129d0e446bde7))
* **website:** publish wiki as Astro site, fix graph builder ([#13](https://github.com/nlamirault/kortex/issues/13)) ([39e0c64](https://github.com/nlamirault/kortex/commit/39e0c643aecc9bedc02b4ea5619d8247aa419524))
* **wiki:** add evolve loop to close wiki-to-procedure cycle ([1f27ea6](https://github.com/nlamirault/kortex/commit/1f27ea6e9d2d6166ec720c63ebf4790d9e27c777))
* **wiki:** add evolve loop to close wiki-to-procedure cycle ([6c8be2c](https://github.com/nlamirault/kortex/commit/6c8be2cb1bb8e52a902ed215cbadec0cc1b2156a))
* **wiki:** add KG extraction, missing skills, and kb build pipeline ([c48b62a](https://github.com/nlamirault/kortex/commit/c48b62abe795562d2485bce0bd4a588835f64ddd))
* **wiki:** add KG extraction, missing skills, and kb build pipeline ([4a3449c](https://github.com/nlamirault/kortex/commit/4a3449ceba445a6ada941f52b9d3a9cd17bdbc20))
* **wiki:** add OKF v0.2 trust signal fields to all pages ([dd5cc54](https://github.com/nlamirault/kortex/commit/dd5cc544ed9b68128dd6d8c3ded477a506dc9196))
* **wiki:** enhance structure with hot cache, skills, and richer frontmatter ([6b06902](https://github.com/nlamirault/kortex/commit/6b069026678e7d3335bfc40e669e6ab61b8228cc))
* **wiki:** initialize Kortex personal knowledge base with LLM wiki protocol ([14b607f](https://github.com/nlamirault/kortex/commit/14b607f7e0507459b5b3ae202f2b998c51d24515))
* **wiki:** reclassify tools to projects/, add sources and people ([93d642e](https://github.com/nlamirault/kortex/commit/93d642e8eeace9b208d1eaaa5ecd4858d0fc621f))


### 🐛 Bug Fixes

* **website:** resolve wiki cross-links to absolute base paths ([#14](https://github.com/nlamirault/kortex/issues/14)) ([f429449](https://github.com/nlamirault/kortex/commit/f4294497e6e5e3024948b40394879a447b411798))
* **wiki:** convert wikilinks to markdown links in domain hub pages ([5a9477c](https://github.com/nlamirault/kortex/commit/5a9477c2115a4c2735be7949b90b6f1dc1e468e7))
* **wiki:** fix broken links and add lychee link checker ([20b2f77](https://github.com/nlamirault/kortex/commit/20b2f77454a4b87278616787d49cb71d337af6c2))
* **wiki:** render cross-reference links as markdown ([#12](https://github.com/nlamirault/kortex/issues/12)) ([9a2d346](https://github.com/nlamirault/kortex/commit/9a2d346a7227c0d041762df48712bc8b227de66d))


### 🚨 Maintenance

* **github:** add repository settings for probot sync ([2381d5f](https://github.com/nlamirault/kortex/commit/2381d5ffe9bfd03debd6bf70190d2495c6de6caf))
* **github:** add repository settings for probot sync ([32e3aca](https://github.com/nlamirault/kortex/commit/32e3aca03fb3fc0663577f1147009b56848332df))
* **wiki:** clear ephemeral sources path from all migrated pages ([009564c](https://github.com/nlamirault/kortex/commit/009564c75e478bd436436752d616f81dafae5206))


### 📚 Documentation

* add Diataxis documentation structure ([#11](https://github.com/nlamirault/kortex/issues/11)) ([3cd2239](https://github.com/nlamirault/kortex/commit/3cd223908cbec5f35f7264fea86a401dd5d34440))
* **decisions:** add ADR-0001 for OKF adoption ([0ba9f5f](https://github.com/nlamirault/kortex/commit/0ba9f5f4a699e959ff1b34880d4492133382aeb1))
* **decisions:** add ADR-0001 for OKF adoption ([d25c602](https://github.com/nlamirault/kortex/commit/d25c602ae82f0e184c100f96bde79dac2c3e8721))
* **kb:** add okf knowledge base migrated from notion ([456ca29](https://github.com/nlamirault/kortex/commit/456ca2909dc4b3f570135e88630485a5699f3f01))
* **kb:** add okf knowledge base migrated from notion ([874058a](https://github.com/nlamirault/kortex/commit/874058a378061b3eb9370de0e5bd8571cc5463a0))
* **readme:** mention OKF v0.2 as the wiki page format ([0d31391](https://github.com/nlamirault/kortex/commit/0d313911240ef313a7b5134890958218505a34af))
* **wiki:** /close writes live queue count to hot.md Pending Ingests ([c80a261](https://github.com/nlamirault/kortex/commit/c80a261624cee5b8349fe311f5ed6d062431b62f))
* **wiki:** add /graph skill for SPO Relations table traversal ([6d4298d](https://github.com/nlamirault/kortex/commit/6d4298d2f3945d36ac183bf10ffdfa755697c893))
* **wiki:** add /ingest --fiche mode for article capture ([2933b6e](https://github.com/nlamirault/kortex/commit/2933b6e53bd747e87f2f720a9dd891d39c080948))
* **wiki:** add chronological index and pending ingests tracking ([a65b7fb](https://github.com/nlamirault/kortex/commit/a65b7fbaba9d40ecc16dbf4da568a439096038d8))
* **wiki:** add graph traversal, fiche ingest, and queue tracking ([0a6e81c](https://github.com/nlamirault/kortex/commit/0a6e81c1fbc687f65132cc959f62d76a3be7b8bc))
* **wiki:** add SPO Relations section to entity page templates and ingest workflow ([01ed279](https://github.com/nlamirault/kortex/commit/01ed2795cae6694955b36fa6a1ef4b19c7d1c812))
* **wiki:** enforce stale_after expiry discipline in /lint ([6b908fc](https://github.com/nlamirault/kortex/commit/6b908fc4a1b4070069dfa5ee3666050bc926ef45))
* **wiki:** ingest Machine Payments Protocol from paymentauth.org ([25eb32d](https://github.com/nlamirault/kortex/commit/25eb32db3725fe4f23fb6a4c9f2b318f6e33b530))
* **wiki:** ingest Machine Payments Protocol from paymentauth.org ([290d90b](https://github.com/nlamirault/kortex/commit/290d90b1f3814af5160362525b3299d0075a08cc))
* **wiki:** ingest x402 internet-native payment protocol ([a8faf56](https://github.com/nlamirault/kortex/commit/a8faf56b94bdc64e12513f40d8f778400ecb2b38))
* **wiki:** ingest x402 internet-native payment protocol ([2f23b08](https://github.com/nlamirault/kortex/commit/2f23b081c5478849dc22cd1364925ff59e3aae5a))
* **wiki:** initialize LLM wiki protocol structure ([ca6bdbd](https://github.com/nlamirault/kortex/commit/ca6bdbd4daec5252af4513b12f3d2f7ff169e378))
* **wiki:** migrate notion kb into wiki domains and concepts ([13be1ed](https://github.com/nlamirault/kortex/commit/13be1ed90412acc334b7e531330213554a5ea9ec))
* **wiki:** surface ingest queue in /today session briefing ([8111cba](https://github.com/nlamirault/kortex/commit/8111cba12d0b9bd3f5ff9572c5d35cc5da213d1e))
