package main

import (
	"crypto/md5"
	"fmt"
	"github.com/fatih/color"
	"lab_05/md5pipeline"
	"math"
	"sort"
	"time"
)

func Max(x, y int64) int64 {
	if x < y {
		return y
	}
	return x
}

func Min(x, y int64) int64 {
	if x > y {
		return y
	}
	return x
}

func handle(results []md5pipeline.ResultingOutput, startT time.Time, realTime int64, verbose bool, measures bool) {
	var (
		total int64 = 0

		fileScannerDuration int64
		waitingForDigester  int64
		digesterDuration    int64
		waitingForAggregate int64
		aggregateDuration   int64
	)

	boldGreen := color.New(color.FgGreen, color.Bold)
	boldRed := color.New(color.FgRed, color.Bold)
	boldBlue := color.New(color.FgBlue, color.Bold)

	sort.Slice(results, func(i, j int) bool {
		return results[i].Start1.Before(results[j].Start1)
	})

	var maxQueue int64 = -1
	var minQueue int64 = math.MaxInt64

	var maxLine int64 = -1
	var minLine int64 = math.MaxInt64

	var maxAll int64 = -1
	var minAll int64 = math.MaxInt64

	for i, res := range results {
		total++

		if verbose {
			boldGreen.Printf("Tape 1\tTask %d\t\t%.2fµs\t%.2fµs\n", i+1, float64(res.Start1.Sub(startT).Nanoseconds())*1e-3, float64(res.End1.Sub(startT).Nanoseconds())*1e-3)
			boldRed.Printf("Tape 2\tTask %d\t\t%.2fµs\t%.2fµs\n", i+1, float64(res.Start2.Sub(startT).Nanoseconds())*1e-3, float64(res.End2.Sub(startT).Nanoseconds())*1e-3)
			boldBlue.Printf("Tape 3\tTask %d\t\t%.2fµs\t%.2fµs\n", i+1, float64(res.Start3.Sub(startT).Nanoseconds())*1e-3, float64(res.End3.Sub(startT).Nanoseconds())*1e-3)
		}

		currFsDur := res.End1.Sub(res.Start1).Nanoseconds()
		currDigDur := res.End2.Sub(res.Start2).Nanoseconds()
		currAggDur := res.End3.Sub(res.Start3).Nanoseconds()
		currSummaryLine := currAggDur + currDigDur + currFsDur

		currSummaryQueue := res.WaitingForDigester.Nanoseconds() + res.WaitingForAggregation.Nanoseconds()
		currSummaryAll := currSummaryQueue + currSummaryLine

		maxLine = Max(maxLine, currSummaryLine)
		minLine = Min(minLine, currSummaryLine)

		maxQueue = Max(maxQueue, currSummaryQueue)
		minQueue = Min(minQueue, currSummaryQueue)

		maxAll = Max(maxAll, currSummaryAll)
		minAll = Min(minAll, currSummaryAll)

		fileScannerDuration += currFsDur
		waitingForDigester += res.WaitingForDigester.Nanoseconds()
		digesterDuration += currDigDur
		waitingForAggregate += res.WaitingForAggregation.Nanoseconds()
		aggregateDuration += currAggDur
	}

	fmt.Printf("Total files:\t\t%v\n", total)
	fmt.Printf("Real time spent (µs):\t%.2f\n", float64(realTime)*1e-3)

	fmt.Printf("Average queue #2 (µs):\t%.2f\n", float64(waitingForDigester)/float64(total)*1e-3)
	fmt.Printf("Average queue #3 (µs):\t%.2f\n", float64(waitingForAggregate)/float64(total)*1e-3)

	fmt.Printf("Average line #1 (µs):\t%.2f\n", float64(fileScannerDuration)/float64(total)*1e-3)
	fmt.Printf("Average line #2 (µs):\t%.2f\n", float64(digesterDuration)/float64(total)*1e-3)
	fmt.Printf("Average line #3 (µs):\t%.2f\n", float64(aggregateDuration)/float64(total)*1e-3)

	fmt.Printf("Min queue (µs):\t\t%.2f\n", float64(minQueue)*1e-3)
	fmt.Printf("Average queue (µs):\t%.2f\n", float64(waitingForDigester+waitingForAggregate)/float64(total)*1e-3)
	fmt.Printf("Max queue (µs):\t\t%.2f\n", float64(maxQueue)*1e-3)

	fmt.Printf("Min line (µs):\t\t%.2f\n", float64(minLine)*1e-3)
	fmt.Printf("Average lines (µs):\t%.2f\n", float64(fileScannerDuration+digesterDuration+aggregateDuration)/float64(total)*1e-3)
	fmt.Printf("Max line (µs):\t\t%.2f\n", float64(maxLine)*1e-3)

	fmt.Printf("Min all (µs):\t\t%.2f\n", float64(minAll)*1e-3)
	fmt.Printf("Average all (µs):\t%.2f\n", float64(fileScannerDuration+waitingForDigester+digesterDuration+waitingForAggregate+aggregateDuration)/float64(total)*1e-3)
	fmt.Printf("Max all (µs):\t\t%.2f\n", float64(maxAll)*1e-3)

	if measures {
		return
	}

	fmt.Println()
	m := make(map[string][md5.Size]byte)

	for _, r := range results {
		m[r.Path] = r.Sum
	}
	var paths []string
	for path := range m {
		paths = append(paths, path)
	}
	sort.Strings(paths)
	for _, path := range paths {
		fmt.Printf("%10x  %s\n", m[path], path)
	}
}
