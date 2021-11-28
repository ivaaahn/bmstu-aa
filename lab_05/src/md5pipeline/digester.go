package md5pipeline

import (
    "crypto/md5"
    "io/ioutil"
    "time"
)

func digester(done <-chan struct{}, fsOutputChan <-chan fileScannerOutput, digesterOutputChan chan<- digesterOutput) {
    for fileInfo := range fsOutputChan {
        startT := time.Now()
        fileData, err := ioutil.ReadFile(fileInfo.path)

        checksum := md5.Sum(fileData)

        select {
        case digesterOutputChan <- digesterOutput{
            fileInfo.path,
            checksum,
            err,
            fileInfo.startTime,
            fileInfo.endTime,
            startT.Sub(fileInfo.endTime),
            startT,
            time.Now(),
        }:
        case <-done:
            return
        }
    }
}
