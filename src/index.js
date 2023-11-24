const { build } = require("./scripts/builder");

const scripts = {
	build: "build"
}

const args = {
	dev: "dev"
}

require.main === module && (async _ => {
	const argv = process.argv.slice(2).map(x => x.toLocaleLowerCase());
	const script = argv[0];
	const isDev = argv.length > 1 && argv.includes(args.dev);
	
	switch (script) {
		case scripts.build:
			await build(isDev);
			break;
		default:
			console.log("invalid command");
			break;
	}
})();