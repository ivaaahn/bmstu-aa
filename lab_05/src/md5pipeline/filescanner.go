package md5pipeline

import (
	"errors"
	"os"
	"path/filepath"
	"time"
)

func scanFiles(done <-chan struct{}, root string) (<-chan fileScannerOutput, <-chan error) {
	fileScanOutputChan := make(chan fileScannerOutput, queueSize)
	scanErrors := make(chan error, 1)

	go func() {
		defer close(fileScanOutputChan)
		startTime := time.Now()
		scanErrors <- filepath.Walk(root, func(path string, info os.FileInfo, err error) error {
			if err != nil {
				return err
			}

			if !info.Mode().IsRegular() {
				return nil
			}

			select {
			case fileScanOutputChan <- fileScannerOutput{
				path,
				startTime,
				time.Now(),
			}:
				startTime = time.Now()
			case <-done:
				return errors.New("scanning was canceled")
			}

			return nil
		})
	}()

	return fileScanOutputChan, scanErrors
}
