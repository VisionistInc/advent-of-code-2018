const input = require("./input.js");

const matrixRight = input.reduce((acc, curr) => Math.max(curr.left, acc), 0) + input.reduce((acc, curr) => Math.max(curr.width, acc), 0) + 1;
const matrixTop = input.reduce((acc, curr) => Math.max(curr.top, acc), 0) + input.reduce((acc, curr) => Math.max(curr.height, acc), 0) + 1;
const matrixLeft = input.reduce((acc, curr) => Math.min(curr.left, acc), 99999999999999999999);
const matrixBottom = input.reduce((acc, curr) => Math.min(curr.top, acc), 99999999999999999999);

let theMatrix = Array(matrixRight);
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// ,,,,,,,,,,,,,,,,,,,,,cccccccccccccccccccccccccccccccCAAAAARRRRRAASSSTTTTTTTTTTTTTTTTTTCCcccccccccccc,,,,,,,,,,,,,,,,   ,,,,,,,,ccssTTTTCc,                             ,,,,,,,,,cccccccccccccccc,,,,,,
//                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cSSAAAARRARSTSTTCCCCCCCCCCCCCCCCCCCCccc,,,c,,,,,,,,,  ,                  ,,,ccssCcCsc,                                  ,,,,,,,,,,,,,,cccc,,,,
//                  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CCSSTSRARSTTCTTTCCTCCCCCCCCCCCCCCCcccc,,,,,,,,,,,,,                      ,,cscCsc,cc                                   ,,,,,,,,,,,,,,,,,,,,,,
//                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,sTTTTARRRTCCCCCCCCCCCCCCCCCCCCCsscsccc,,,,,,,c,,,,,                       ,cCcTcc  c                                   ,,,,,,,,,,,,,,,,,,,,,,,,
//                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CTsCTTARATssssCCCCCCCCCCCCCCCsCCsccccc,,, ,,,c,,,,,                       ,,TTccc,                                     ,,,,,,,,,,,,,,,cccc,,,,
//                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CCCCCCSARCccsCCCCCCCCCCCCCsCCCsCscccccc,,,,,,,,,,,,,                      ,ccC,c ,                                     ,,,,,,,,,,,,,,c,,,,,,,,
//                ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CsCCCCARRCsssssCsCCCCCCCCCCCsCCCssccccc,,, ,,,,,,,,  ,                     ,c,                                            ,,,,,,,,,,,,,,,,,,,,
//              , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,sCCCCCARACCCCsssCCCCTTTCTTCCCCCCCcccccc,,, ,c,,,,,,, ,,                    ,c                                                ,,,,,,,,,,,,,,,,,
//                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CCTTSTSSScCCSSSARRRARRRASSTTTCCCCsCCCCsc,,,,c,,c,,,,,,,,  ,,,,,,cssCsscccc,,c                                                    ,,,,,,,,, ,,  ,
//                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cCTTSSTSSSAARAASSRRRRRRRRRRRRASTCcccsCCCcc,,cc,,c,c,,,,,,,cCSTSSSTSTTTCccccccc,,,,                                                 ,  , ,
//              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CTSSSTTSATRRRARRSRRRRRRRRRRRRRRRRSCcccCCCc,,ccc,,cccccsSSSSSSSSSSSSTTTTcccccccsc,,,
//             ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CTSSTCCSSCSSRRRRRRRRRRRRRRRRRRRRRRRASTCTTTccc,cccTTSAAAARRARRAASSTTTTTSCCccccC,c,,,,
//                ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,TTSTTCCTSCTARRRRRRRRRRRRRRRRRRRRRRRRRRRsRTCccccCTSAAAAARARRRRRAAASSTTTTccccccc ,,,,,
//           , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,sCTTTTCTTscRRRRRRRRARRRRRRRRRRRRRRRRRRTRRASSTCTCCTTTSSAARARRRASASSSSTTCcccccc, ,,,,,
//            ,,, ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CCTTTCTScssRRRRRRRRRRRRRRRRRRRRRRRRRRRRRATTCCsscSAAAAAASAAAARSTSTTTTTsccccc , ,,,,
//            , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cCTSCCTccsCRRRRRRRSRRRRRRRRRRRRRRRRRRRAATccccccCSSAAAASAAAASSTTTTCTCccccc    ,,,                                                              ,,
//   ,,         ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cCTTTCCssssCARRRRRRRRRRRRRRRRRRRRRRRRRASCc,, cscTSASSSSSSSSSSTTTTTTCcccc     ,,                                                     ,,,,,,,,,,,,,,
//        , ,,, ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,csCTTCCccssCCTRRRRRRRRRRRRRRRRRRRRRRAASCscc,  ,cccSSSSSSSSSSSTSTTTTccc      ,,,                                            ,,,,,,,,,,,,,,,,,,,,,,,
//         ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,sCCCCCccssCCCCTRRRRRRRRRRRRRRRAARARSSTCcc,,   ,ccsSSSSSSSSSSSTTTTcc                                                    ,,,,,,,,,,,,,,,,,,,,,,,,,,
//      , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CsCCTCccsCCCCCTTTRRRRRRRRRRRRRRRRAASTCCcc,,    ,ccTSSSSSSSSSTTCC,                                              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccc
//  ,   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CCCCCccccCCCCCTTTTTARRRRRRRRRRRSSTTCCCsc,,      ccccsCCCCsc,                                               ,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccccc
//       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,CCCCscscCCCCCCCCCTTTTTTTTTTTTTTCTCCCCcc,,,           , ,,                                           ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccccccccccc
//      , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cscccscCCCCCCTCTCCTCCTCTCCTTTTCCCCCCCcc,,        ,     ,              ,                               ,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccccccc
//     ,, ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccsCCCTTCTTTCCTTTCCCCCCCCCCCCCCCscc,,                            ,                                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccccccsss
//      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccsCCCCTTTTCCCCCCCCCCCCCCCCCCCCCscc,,         ,                                                 ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccccccsss
//   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccccsCCCTTTTTTTCCCCCCCCCCCCCCCCCCCscc,,                                                         ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccccscss
//   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccCCTTTTTTTTCCCCCCCCCCCTCCCCCCCscc,,        ,                                              ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccccccscss
//  , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccsCCTTTTTTCTCCCCCCCCCCCTTCTCCCCscc,,       ,,,                                            ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,c,,,,,ccccccccsss
//  , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,c,cccccccssCCTTTTTTTTTCCCCCCCCTTTCCCCCCCCcc,,       ,,,,,                                       , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccc,ccccccccsss
//       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccccccCCTTTTTTCCCCTCCCCCTTTTCCCCCCCCcc,,        ,,,,               ,,                       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccccccccccccssss
//       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccccccsCCTTTTTCCCTTCCCCTTTTCCCCTTCTCCsc,,        ,,,,,              ,,                      ,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccccccccccccccccccsss
//       , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccSTCCCCTTTTTCCCCTCCCTTTCCCCTSASSSCCc,,  cCc,,  ,,,,              ,,                      ,,,,,,,,,,,,,,,,,,,,,,,,,,,cccccccccccccccccccssCs
//       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccSRRCCCCTTTTTCCCTCTTTTTTCCCCCTTTTSTCC,,   ,      ,,,             ,,,,                     ,,,,,,,,,,,,,,,,,,,,,cc,,cccccccccccccccccccccssCC
//       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccTRARCCCCTTTTCCCCCCCCTTTCCCCTCCTTTTTTCc,           ,              ,,,,,c,,,,Cc,            , ,,,,,,,,,,,,,,,,,,cccccccccccccccccccccccccssCCC
//       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccRRARRCCCTTCTCTCCCCCTTTCTCCCTTTTTTTCccc,,          ,,            , ,,,cTsccCTc,,,          ,,,,,,,,,,,,,,,c,ccccccccccccccccccccccccccccssCCC
//      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,SRRRRRCCCTTTTTTCCCCCTTTTTTTTTTTTTTTccc,,,,   ,                   c   ,cTCsssCscc,,          ,,,,,,,,,,,,,,cccccccccccccccccccccccccccccccCCCC
//       ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cRRRRRRSCCCCCTTCCCTCCTTTTTTTTTTTTTTCc,cc,,,                      CCc  ,cccCCccCCTc,,,      ,,,,,,,,,,,,,,cccccccccccccccccccccccccccccccccssss
//      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cScccsSc,,,,,,,,,,,,cRRRRRRRACCCTTTTCCCTTTTTTTTTTTTTTTCCcc,ccc,                       TTTCccccccccccsCcccc,,,,,,,,,,,,,,,,,,,,ccccccccccccccccccccccccccccccccccsCC
// ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cSSTTSSc,,,,,,,,,,,,RRRRRRRRRCCCTTTTCTCTTTTTTTTTTTTCTTCCc,,,c,,,        ,            ,TSASSSTsccccCCCTCsCsc,,,,,,,,,,,,,,,,,,ccccccccccccccccccccccccccccccccccssCs
//     ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cCCssCTscc,,,,,,,,,CRRRRRRRRRTCCTTCCTCCTTTTSSSTSTTTTSSTSTccc,,,,,,,,,  ,,,,          ,TTAASSTsCccCCCCTSSSTc,,,,,,,,,,,,,,,,,ccccccccccccccccccccccccccccccccccccsCC
// ,   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccCTSSSTCCc,,,,,,,cARRRRRRRRRSTCCTTCCCTTTTTSSSSSTSSTTSSTCssCsccTTTTTsCccc,,          CTTSASCsccCTSCCCTSARAC,,,,,,,,,,,,,,,ccccccccccccccccccccccccccccccccccccccsCC
//     ,,,,,,,,,,,,,,,,,,,,,,,,,,,,CSASCCCCCTTTTCCTc,,,,,cRRRRRRRRRRRRCTCTTTCCTTTTTSSSSSSSSSCscccTTCc,,c,TSc,, ,,,,          TTSSSCscccCSASTSSARRRSc,,,,,,,,,,,,cccccccccccccccccccccccccccccccccccccccsssC
// ,   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,ARRSTTsccCCCCsCCCc,,,cRRRRRRRRRRRRRTTTCTTCCTTTTTSTTTTSTCc,cccc,,,, ,c,cc,    ,,,          TTTCcccccCSSAASSSARRATscc,,,,,,,,,,c,cccccccccccccccccccccccccccccccccccccssCC
//     ,,,,,,,,,,,,,,,,,,,,,,,,,,ccAAASTTTTTTTTTTTTTTCccTRRRRRRRRRRRRRSTTTTCTTTTTTTTTTTTTTTTccccc,,,,,c,,,, ,    ,,          STccc,,cCSSARRASSTTTTTsccc,,,,,,,,,cccccccccccccccccccccccccccccccccccccccssCs
//     ,,,,,,,,,,,,,,,,,,,,,,,,,,CASSTCssCSSSSSSASSCsccSRRRRRRRRRRRRRRSTTTCTCTTTTTTTTTTTTTTTTcccc,,,,,,,,,,,      ,         cSScc,,,cTASAARAASTTTTTCccc,,,,,,,ccccccccccccccccccccccccccccccccccccccccccccc
//     ,,,,,,,,,,,,,,,,,,,,,,,,,,csTTsccCTSSSSAARRAscccARRRRRRRRRRRRRRRSTTTTTTTTTSTTTTTCTTTTTCscc,c,,,,,,,,      ,          SSTscc,,cSASSAAASSSSSSSTsccc,,,,ccccccccccccccccccccccccccccccccccccccccccccccc
// ,   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccccCTSASSAARRRRCcccSARRRRRRRRRRRRRRSTTTTTTTTTTTTTTTTTTTSTTTCccc,,,,,,,       ,         cSSSTcc,,cTASSSSASASSSASTsccc,cccccccccccccccccccccccccccccccccccccccccccccccccc
//      ,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccCSAARRAARRRRRSCCCSARRRRRRRRRRRRRRRSSSTTTTTTTTTTTTTTTTTSTTTTTCscc,,,,       ,         SSTTTCcc,cCASSSAASSSSSSSSCssCcsTTSSSSSTTCscccccccccccccccccccccccccccccccccccccc
// ,  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccCARRRRRRRRRRRASTTSARRRRRRRRRRRRRRRASSTTTTTTTTTTTTTTTTTTTTTTTcccc,,,,                cSSSSScccCsCSAASSAAAAASAASTCTSASSAASSSSSSSSSSSASSSSTTCCCscccccccccccccccccccccccc
//   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,ccCAARRRRRRRRRRRASSSARRRRRRRRRRRRRRRRASSTTTTTTTTTTTTTTTTTTTCCcsccc,,,,                SSSTSTccCASAASSSSAAAAAAASASTSAAASSASASSASSSSSSSSSSSSSSAASASASSTcccccccccccccccccc
//  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,csSRARRRRRRRRRRRAAAAARRRRRRRRRRRRRRRRSSSTTTTSTTTTTTTTTTTCccc,,,,,,,,                cSSSSSTssSASRRASSSARRRAASSSSSSSAAASSSASSASSASSSASSASSSASAAASSSATAASscccccccccccccc
// , ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cccCSARRRRRRRRRRRRRAAASARRRRRRRRRRRRRRRASSSTTTTTTTTTTTTTCCCcccc,,,,,,                cSSSTTSTCCSSSRRAASARRRRRAATSSSTsccccccCTTSSSSASSSSSSAASAAAASASSSSSSSSSCcccccccccccc
//  ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cCTTSAARRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRASSSTTTTTTTTTTTTTCCCcccc,,,,,,              ,SASASSTCCTAAARRRRAARRRRRRAASSCc,,  ,,,,,,,,,csSSSSASSAAARAASSSASSSSAARAAASCcccccccc
// ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,cTASSAASRRRRRRRRRRRAAARRRRRRRRRRRRRRRRRRRASSSTTTTTTTSTTTTTTTcc,c,,,,, ,            csASAATCCCTSRRARRRRAAAARRRRRASsc,              ,,cSSSAAAAAARSSSAASSAARAAAASASSCcccccc
// ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,csSSTTSSSARRRRRRRRRASSSARRRRRRRRRRRRRRRRRRRSSSTTSTTTTSTTTTTTTCccc,,,,,,,           ,CSRSTCsCCTSSRRRRRRRRARAAARAASc,,                 ,cSSAAASASSSSSSSASRRAASASSSSSSTccccc
// ,,,,,,,,,,,,,,,,,,,,,,,cccCTSRRTTASCTSSSRRRRRRRAARASSTCCTARRRRRRRRRRRRRRRRRSSSSTTTTTSSSSSSTTTsc,,,,,,,,,,        ,sTTTTCCTTSSARRRRRRRRRRRRRAASSc,,,                  ,CSAAAAASSSSSSSSRAASAATSSSSSSSccccc
// ,,,,,,,,,,,,,,,,,,ccTSRRRRRRRRRSTASTTAAARRRRRRASARRASSCCcsCSARRRRRRRRRRRRRRAASSTSTSSTSSSSSSSSTCcc,,,,,,,,       ,sCTTCCTTTSSARRRRRRRRRRRRRRRAACc,,,                   cSSASASATSSSSSRRRASSSSSSSSSSSCcccc
// ,,,,,,,,,,,,,cTARRRRRRAAAAASSSTTSRRAARRRRRRRRRRRRRRAASTTCCcsCTARRRRRRRRRRRRRRASSSTTSSSSSSSSSSSSTCccc,,,,   , ,,cCTTCTTSSSSSAARRRRRRARARARRRRRATc,,                    ,SASSSSSTSSSSRARSASAAARAAARRAScccc
// ,,,,,,,,,cSRRRARRARAASSSTTCCsCCTSARRRRRRRRRRRRRRRRAARAASSTTCCCCTSRRRRRRRRRRRRAASSSSSTSSSSAAATsc,,,,,,,,,, ,,,,ssTTCTTTTSSSSSSSSSSSSSSSSSARRRRATc,,                    ,SSSSSTSTSTSASRRRARARSSSSSSSSSTccc
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
// RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

for (var i = 0; i <= matrixRight; i++) {
  theMatrix[i] = [];
  for(var myvar = 0; myvar <= matrixTop; myvar++) {
    theMatrix[i].push(0);
  }
}

console.warn('t̗̥̻̣h͓̘̞̩͍͖̘͞e ̨͚̦ma̼͢t̘̠̦̳͙͈r͙̗ị͕̗̹̙̣x̪͕͇̥ ̴̬͇̬̠̦̟ḭ̲̱s̹͚̪̼͎̲͖͘ ͎̙̠̜̳r̟̟ea̩̫͇̝d̘̜̪́y̷̳͕!̟̼̣͕̳́');

for (var i = 0; i < input.length; i++) {
  let thing = input[i];
  let width = thing.width,
      height = thing.height,
      left = thing.left,
      top = thing.top;
  for (var x = left; x < width + left; x++) {
    for (var y = top; y < top + height; y++) {
      theMatrix[x][y]++
    }
  }
}

for (var i = 0; i < input.length; i++) {
  let thing = input[i];
  let width = thing.width,
      height = thing.height,
      left = thing.left,
      top = thing.top;

  let foundOverlaps = false;
  for (var x = left; x < width + left; x++) {
    for (var y = top; y < top + height; y++) {
      if (theMatrix[x][y] > 1) foundOverlaps = true; 
    }
  }
  if (!foundOverlaps) throw new Error(thing.id);
}

let count = 0;
theMatrix.forEach(firstThing => {
  firstThing.forEach(secondThing => {
    if (secondThing > 1) ++count;
  })
})
throw new Error( `COUNT: ${count}`)