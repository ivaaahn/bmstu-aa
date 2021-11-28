package md5pipeline

import (
	"crypto/md5"
	"io/ioutil"
	"os"
	"path/filepath"
	"sync"
	"time"
)

func (p *MD5Pipeline) MD5All(root string) ([]ResultingOutput, error) {
	done := make(chan struct{})
	defer close(done)

	scanOutputChan, scanErrors := scanFiles(done, root)

	digesterOutputChan := make(chan digesterOutput, queueSize)

	var wg sync.WaitGroup
	wg.Add(p.numOfWorkers)

	for i := 0; i < p.numOfWorkers; i++ {
		go func() {
			digester(done, scanOutputChan, digesterOutputChan)
			wg.Done()
		}()
	}

	go func() {
		wg.Wait()
		close(digesterOutputChan)
	}()

	result := make([]ResultingOutput, 0)

	for digesterRes := range digesterOutputChan {
		startTime := time.Now()

		if digesterRes.err != nil {
			return nil, digesterRes.err
		}

		result = append(result, ResultingOutput{
			digesterRes.path,
			digesterRes.sum,
			digesterRes.startFileScannerTime,
			digesterRes.endFileScannerTime,
			digesterRes.waitingTimeInQueue,
			digesterRes.startTime,
			digesterRes.endTime,
			startTime.Sub(digesterRes.endTime),
			startTime,
			time.Now(),
		})
	}

	if err := <-scanErrors; err != nil {
		return nil, err
	}

	return result, nil
}

func (p *MD5Pipeline) MD5AllSerial(root string) ([]ResultingOutput, error) {
	paths := make([]fileScannerOutput, 0)
	hashes := make([]digesterOutput, 0)
	result := make([]ResultingOutput, 0)
	scanErrors := make(chan error, 1)

	startT := time.Now()
	scanErrors <- filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}

		if !info.Mode().IsRegular() {
			return nil
		}

		paths = append(paths, fileScannerOutput{
			path,
			startT,
			time.Now(),
		})

		startT = time.Now()
		return nil
	})

	for _, fileInfo := range paths {
		startT = time.Now()
		fileData, err := ioutil.ReadFile(fileInfo.path)

		checksum := md5.Sum(fileData)

		hashes = append(hashes, digesterOutput{
			fileInfo.path,
			checksum,
			err,
			fileInfo.startTime,
			fileInfo.endTime,
			startT.Sub(fileInfo.endTime),
			startT,
			time.Now(),
		})
	}


	for _, digesterRes := range hashes {
		startT = time.Now()

		if digesterRes.err != nil {
			return nil, digesterRes.err
		}

		result = append(result, ResultingOutput{
			digesterRes.path,
			digesterRes.sum,
			digesterRes.startFileScannerTime,
			digesterRes.endFileScannerTime,
			digesterRes.waitingTimeInQueue,
			digesterRes.startTime,
			digesterRes.endTime,
			startT.Sub(digesterRes.endTime),
			startT,
			time.Now(),
		})
	}

	if err := <-scanErrors; err != nil {
		return nil, err
	}

	return result, nil
}
