package main

import (
    "fmt"
    "github.com/akamensky/argparse"
    "lab_05/md5pipeline"
    "log"
    "os"
    "time"
)

func main() {
	parser := argparse.NewParser("md5pipeline", "Hashing files in directory")

	verbose := parser.Flag(
		"v", "verbose", &argparse.Options{Help: "Verbose mode"},
	)

    measures := parser.Flag(
        "m", "measures", &argparse.Options{Help: "Show only measures"},
    )

    serialMode := parser.Flag(
        "s", "serial", &argparse.Options{Help: "Serial Mode"},
    )

    path := parser.String(
        "p", "path", &argparse.Options{
            Required: true,
            Help: "Path to file (dir)",
        },
    )

    numberOfWorkers := parser.Int(
        "n", "numberOfWorkers", &argparse.Options{
            Required: false,
            Help: "Number of digester workers",
        },
    )

    err := parser.Parse(os.Args)
    if err != nil {
        log.Fatalln(parser.Usage(err))
        return
    }


    if *numberOfWorkers == 0 {
        *numberOfWorkers = 16
    }

	pipeline := md5pipeline.NewPipeline(*numberOfWorkers)

	startT := time.Now()

    var data []md5pipeline.ResultingOutput

    if *serialMode {
        data, err = pipeline.MD5AllSerial(*path)
    } else {
        data, err = pipeline.MD5All(*path)
    }

	if err != nil {
		fmt.Println(err)
		return
	}

	handle(data, startT, time.Since(startT).Nanoseconds(), *verbose, *measures)
}
