package md5pipeline

import (
	"crypto/md5"
	"time"
)

const queueSize int = 69257


type fileScannerOutput struct {
	path string

	startTime time.Time
	endTime   time.Time
}

type digesterOutput struct {
	path string
	sum  [md5.Size]byte
	err  error

	startFileScannerTime time.Time
	endFileScannerTime   time.Time

	waitingTimeInQueue time.Duration
	startTime          time.Time
	endTime            time.Time
}

type ResultingOutput struct {
	Path string
	Sum  [md5.Size]byte

	Start1 time.Time
	End1   time.Time

	WaitingForDigester time.Duration
	Start2             time.Time
	End2               time.Time

	WaitingForAggregation time.Duration
	Start3                time.Time
	End3                  time.Time
}
