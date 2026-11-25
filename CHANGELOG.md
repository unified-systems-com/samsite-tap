# Changelog

## [0.2.8](https://github.com/unified-systems-com/samsite-tap/compare/v0.2.7...v0.2.8) (2026-11-25)


### Bug Fixes

* **ci:** raise requires_tap floor to 0.4.9 for build_header ([723f695](https://github.com/unified-systems-com/samsite-tap/commit/723f69540bbf1b5af623a50b82d19002103369b4))
* **grift:** the compliance collector writes core's format "1" header instead of "0" ([c527308](https://github.com/unified-systems-com/samsite-tap/commit/c527308ef2ebc451698db740198c84c4308a71c2))
* **grift:** the compliance collector writes core's format "1" header instead of "0" ([f01a78c](https://github.com/unified-systems-com/samsite-tap/commit/f01a78c282ff44f774a57977e7663f40dbf4e8a2))

## [0.2.7](https://github.com/unified-systems-com/samsite-tap/compare/v0.2.6...v0.2.7) (2026-11-25)


### Bug Fixes

* **grift:** drop retired landing_page and HOSTS_DOCUMENT records; restamp to format "1" ([05788f5](https://github.com/unified-systems-com/samsite-tap/commit/05788f523eafd791e3b25efd3960cc0aa5795c1a))
* **grift:** drop retired landing_page and HOSTS_DOCUMENT records; restamp to format "1" ([166deca](https://github.com/unified-systems-com/samsite-tap/commit/166deca4a37bfaf4859f4329153706e004d62fa6))

## [0.2.6](https://github.com/unified-systems-com/samsite-tap/compare/v0.2.5...v0.2.6) (2026-11-20)


### Bug Fixes

* **boot:** the product record names samsite v0.2.5 at its own commit ([1456626](https://github.com/unified-systems-com/samsite-tap/commit/14566269cef2e968806e8086c1d62363f4b1b66b))
* **boot:** the product record names samsite v0.2.5 at its own commit ([65ea52e](https://github.com/unified-systems-com/samsite-tap/commit/65ea52ecf087bc2658910967ff7b95bb8996f339))

## [0.2.5](https://github.com/unified-systems-com/samsite-tap/compare/v0.2.4...v0.2.5) (2026-11-16)


### Features

* **ci:** add the hourly product-health check (tap[#888](https://github.com/unified-systems-com/samsite-tap/issues/888)) ([79d78de](https://github.com/unified-systems-com/samsite-tap/commit/79d78debe2550cbba46315b4d3318b860fe84f76))
* **ci:** add the hourly product-health check [via bom-bom-support] ([fb6b822](https://github.com/unified-systems-com/samsite-tap/commit/fb6b822be96052928c3a4169996e37f8c71e5903))
* drop Readers; scope the landing's people to samsite's own ([44cdcca](https://github.com/unified-systems-com/samsite-tap/commit/44cdccaf942807f541d32c65261fd743021d7576))
* the samsite people are identity_core humans, not computing_core users ([3de44f7](https://github.com/unified-systems-com/samsite-tap/commit/3de44f727be30625b529fe1de5df36fdeda96ebc))
* the samsite people are identity_core humans, not computing_core users [via highbar] ([634a393](https://github.com/unified-systems-com/samsite-tap/commit/634a393e12acd93ca68d7dc3eec72ff31c1e05c3))


### Bug Fixes

* **boot:** pin the commit beside every git source's rev in the CI record ([d30a38a](https://github.com/unified-systems-com/samsite-tap/commit/d30a38acfa1e90b5cc445d61c4f8ed5298ba4053))
* **boot:** pin the commit beside every git source's rev in the CI record [via bom-bom] ([2bc2e1f](https://github.com/unified-systems-com/samsite-tap/commit/2bc2e1fc470c201569b577175978ff505e6c68cc))
* **boot:** pin the releases that carry Dimension seeds; install compliance_core before github_core ([91512f2](https://github.com/unified-systems-com/samsite-tap/commit/91512f21cc03b1898b9c3706f839e3ec0ac39ba9))
* **boot:** pin the releases that carry Dimension seeds; install compliance_core before github_core ([228a608](https://github.com/unified-systems-com/samsite-tap/commit/228a6083244852985cc8551b32c6fed0a2297d7e))
* **ci:** raise requires_tap floor to 0.2.0; drop the nightly's latest-release row ([9f2dcb7](https://github.com/unified-systems-com/samsite-tap/commit/9f2dcb7595c1945dacf821309aee26c5f9c6b4a4))
* **ci:** raise requires_tap floor to 0.2.0; drop the nightly's latest-release row [via bom-bom] ([56c1e29](https://github.com/unified-systems-com/samsite-tap/commit/56c1e29ba5189358708d6307adadea111f00207a))
* **compliance-collector:** parenthesize the multi-exception except clause ([30a1b00](https://github.com/unified-systems-com/samsite-tap/commit/30a1b0004fd3e496e2a072ded36dc7713b6f919a))
* **deps:** pin the product record's plugins by commit ([3680940](https://github.com/unified-systems-com/samsite-tap/commit/36809409fda77211808ee07d23a50ce4c02316e4))
* **deps:** raise compliance-core floor to 0.4.0, matching github_core ([51b3633](https://github.com/unified-systems-com/samsite-tap/commit/51b36334debf8cc387ed70662eb1560b271ff13a))
* **deps:** raise compliance-core floor to 0.4.0, matching github_core ([6709e76](https://github.com/unified-systems-com/samsite-tap/commit/6709e76c8c1ae767351bd0ecf7b1a9dcaefd18c0))
* **edges:** retarget the four renamed-edge waves (computing/compliance/sigstore/aws_core) and pin their releases ([f98d1f3](https://github.com/unified-systems-com/samsite-tap/commit/f98d1f30418120e28cc907a9166934db299e89ed))
* **edges:** retarget the four renamed-edge waves and pin the releases that carry them ([4143c71](https://github.com/unified-systems-com/samsite-tap/commit/4143c71b7cdd40e237035c9c73893394025e5a30))
* **manifest:** raise the tap floor to 0.3.0 ([0c06378](https://github.com/unified-systems-com/samsite-tap/commit/0c063788d07f484142e36a15085789b5aa66a486))


### Documentation

* **grift:** cite issues, not session rulings, in seed descriptions ([1e2964e](https://github.com/unified-systems-com/samsite-tap/commit/1e2964eb08b74ecd93de25f80a7f94a2d01c7334))
* **readme:** focus on the demo; standup moves to the operator guide ([95104e1](https://github.com/unified-systems-com/samsite-tap/commit/95104e136bbb562a39b61b5455d033839bd97f6b))
* **readme:** lead with the boundary graph ([580ab79](https://github.com/unified-systems-com/samsite-tap/commit/580ab79a1ae79c8ea721a5cd66477222d79cc0be))
* **readme:** move the plugin-ownership block to the bottom ([ea334c0](https://github.com/unified-systems-com/samsite-tap/commit/ea334c04171070bdcefd3f190e94484d6fd62f3f))
* **readme:** screenshot tour for compliance audiences ([6a08060](https://github.com/unified-systems-com/samsite-tap/commit/6a0806042be68a925fd70a0e3bb4200e385d3952))
