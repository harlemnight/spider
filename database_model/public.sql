/*
 Navicat PostgreSQL Data Transfer

 Source Server         : postgre12
 Source Server Type    : PostgreSQL
 Source Server Version : 120003
 Source Host           : localhost:5432
 Source Catalog        : DB_FINANCE
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 120003
 File Encoding         : 65001

 Date: 02/02/2021 18:00:49
*/


-- ----------------------------
-- Table structure for t_china_index_1990_2010
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_index_1990_2010";
CREATE TABLE "public"."t_china_index_1990_2010" (
  "index_date" varchar(20) COLLATE "pg_catalog"."default",
  "idd" int4 NOT NULL
)
;

-- ----------------------------
-- Table structure for t_china_security_list
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_security_list";
CREATE TABLE "public"."t_china_security_list" (
  "type" varchar(30) COLLATE "pg_catalog"."default",
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(300) COLLATE "pg_catalog"."default",
  "market" varchar(30) COLLATE "pg_catalog"."default",
  "market_name" varchar(255) COLLATE "pg_catalog"."default",
  "syldt" numeric(255,6),
  "sjl" numeric(255,6)
)
;
COMMENT ON COLUMN "public"."t_china_security_list"."type" IS 'stock(股票)，index(指数)，etf(ETF基金)，fja（分级A），fjb（分级B），fjm（分级母基金），mmf（场内交易的货币基金）open_fund（开放式基金）, bond_fund（债券基金）, stock_fund（股票型基金）, QDII_fund（QDII 基金）, money_market_fund（场外交易的货币基金）, mixture_fund（混合型基金）, options(期权)';
COMMENT ON COLUMN "public"."t_china_security_list"."symbol" IS '标的代码';
COMMENT ON COLUMN "public"."t_china_security_list"."symbol_name" IS '标的名称';
COMMENT ON COLUMN "public"."t_china_security_list"."market" IS '市场代码';
COMMENT ON COLUMN "public"."t_china_security_list"."market_name" IS '市场名称';
COMMENT ON COLUMN "public"."t_china_security_list"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_security_list"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_security_market
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_security_market";
CREATE TABLE "public"."t_china_security_market" (
  "pre_symbol" varchar(10) COLLATE "pg_catalog"."default",
  "market" varchar(10) COLLATE "pg_catalog"."default",
  "market_name" varchar(255) COLLATE "pg_catalog"."default",
  "type" varchar(30) COLLATE "pg_catalog"."default",
  "market_lx" varchar(10) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_security_market"."pre_symbol" IS '标的代码前缀';
COMMENT ON COLUMN "public"."t_china_security_market"."market" IS '市场代码用于获取网易股票历史价格行情用';
COMMENT ON COLUMN "public"."t_china_security_market"."market_name" IS '市场名称';
COMMENT ON COLUMN "public"."t_china_security_market"."type" IS '标的类型';
COMMENT ON COLUMN "public"."t_china_security_market"."market_lx" IS '市场代码用于其他使用SH,SZ的地方如东财';

-- ----------------------------
-- Table structure for t_china_stock_area_eastmoney
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_area_eastmoney";
CREATE TABLE "public"."t_china_stock_area_eastmoney" (
  "area_dm" varchar(12) COLLATE "pg_catalog"."default",
  "area_name" varchar(300) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_area_eastmoney"."area_dm" IS '区域代码';
COMMENT ON COLUMN "public"."t_china_stock_area_eastmoney"."area_name" IS '区域名字';

-- ----------------------------
-- Table structure for t_china_stock_area_eastmoney_dzb
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_area_eastmoney_dzb";
CREATE TABLE "public"."t_china_stock_area_eastmoney_dzb" (
  "area_dm" varchar(30) COLLATE "pg_catalog"."default",
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_area_eastmoney_dzb"."area_dm" IS '区域代码';
COMMENT ON COLUMN "public"."t_china_stock_area_eastmoney_dzb"."symbol" IS '股票代码';
COMMENT ON COLUMN "public"."t_china_stock_area_eastmoney_dzb"."symbol_name" IS '股票名称';

-- ----------------------------
-- Table structure for t_china_stock_concept_10jqka
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_concept_10jqka";
CREATE TABLE "public"."t_china_stock_concept_10jqka" (
  "concept_dm" varchar(12) COLLATE "pg_catalog"."default",
  "concept_name" varchar(300) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_concept_10jqka"."concept_dm" IS '概念代码';
COMMENT ON COLUMN "public"."t_china_stock_concept_10jqka"."concept_name" IS '概念名字';

-- ----------------------------
-- Table structure for t_china_stock_concept_10jqka_dzb
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_concept_10jqka_dzb";
CREATE TABLE "public"."t_china_stock_concept_10jqka_dzb" (
  "concept_dm" varchar(30) COLLATE "pg_catalog"."default",
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_concept_10jqka_dzb"."concept_dm" IS '概念代码';
COMMENT ON COLUMN "public"."t_china_stock_concept_10jqka_dzb"."symbol" IS '股票代码';

-- ----------------------------
-- Table structure for t_china_stock_concept_eastmoney
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_concept_eastmoney";
CREATE TABLE "public"."t_china_stock_concept_eastmoney" (
  "concept_dm" varchar(12) COLLATE "pg_catalog"."default",
  "concept_name" varchar(300) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_concept_eastmoney"."concept_dm" IS '概念代码';
COMMENT ON COLUMN "public"."t_china_stock_concept_eastmoney"."concept_name" IS '概念名字';

-- ----------------------------
-- Table structure for t_china_stock_concept_eastmoney_dzb
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_concept_eastmoney_dzb";
CREATE TABLE "public"."t_china_stock_concept_eastmoney_dzb" (
  "concept_dm" varchar(30) COLLATE "pg_catalog"."default",
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_concept_eastmoney_dzb"."concept_dm" IS '概念代码';
COMMENT ON COLUMN "public"."t_china_stock_concept_eastmoney_dzb"."symbol" IS '股票代码';
COMMENT ON COLUMN "public"."t_china_stock_concept_eastmoney_dzb"."symbol_name" IS '股票名称';

-- ----------------------------
-- Table structure for t_china_stock_finance_dupont
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_finance_dupont";
CREATE TABLE "public"."t_china_stock_finance_dupont" (
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "rq" date,
  "cbze" varchar(30) COLLATE "pg_catalog"."default",
  "ch" varchar(30) COLLATE "pg_catalog"."default",
  "cqdtfy" varchar(30) COLLATE "pg_catalog"."default",
  "cqgqtz" varchar(30) COLLATE "pg_catalog"."default",
  "cwfy" varchar(30) COLLATE "pg_catalog"."default",
  "cyzdqtz" varchar(30) COLLATE "pg_catalog"."default",
  "dysdszc" varchar(30) COLLATE "pg_catalog"."default",
  "fldzc" varchar(30) COLLATE "pg_catalog"."default",
  "fzze" varchar(30) COLLATE "pg_catalog"."default",
  "gdzc" varchar(30) COLLATE "pg_catalog"."default",
  "glfy" varchar(30) COLLATE "pg_catalog"."default",
  "gsmgsgddjlr" varchar(30) COLLATE "pg_catalog"."default",
  "gyjzbdsy" varchar(30) COLLATE "pg_catalog"."default",
  "hbzj" varchar(30) COLLATE "pg_catalog"."default",
  "jlr" varchar(30) COLLATE "pg_catalog"."default",
  "jyxjrzc" varchar(30) COLLATE "pg_catalog"."default",
  "jzcsyl" varchar(30) COLLATE "pg_catalog"."default",
  "kfzc" varchar(30) COLLATE "pg_catalog"."default",
  "kgcsjrzc" varchar(30) COLLATE "pg_catalog"."default",
  "ldzc" varchar(30) COLLATE "pg_catalog"."default",
  "qjfy" varchar(30) COLLATE "pg_catalog"."default",
  "qtfldzc" varchar(30) COLLATE "pg_catalog"."default",
  "qtldzc" varchar(30) COLLATE "pg_catalog"."default",
  "qtysk" varchar(30) COLLATE "pg_catalog"."default",
  "qycs" varchar(30) COLLATE "pg_catalog"."default",
  "sdsfy" varchar(30) COLLATE "pg_catalog"."default",
  "srze" varchar(30) COLLATE "pg_catalog"."default",
  "sy" varchar(30) COLLATE "pg_catalog"."default",
  "tzsy" varchar(30) COLLATE "pg_catalog"."default",
  "tzxfdc" varchar(30) COLLATE "pg_catalog"."default",
  "wxzc" varchar(30) COLLATE "pg_catalog"."default",
  "xsfy" varchar(30) COLLATE "pg_catalog"."default",
  "yfzk" varchar(30) COLLATE "pg_catalog"."default",
  "yszk" varchar(30) COLLATE "pg_catalog"."default",
  "yycb" varchar(30) COLLATE "pg_catalog"."default",
  "yyjlrl" varchar(30) COLLATE "pg_catalog"."default",
  "yysjjfj" varchar(30) COLLATE "pg_catalog"."default",
  "yysr" varchar(30) COLLATE "pg_catalog"."default",
  "yywsr" varchar(30) COLLATE "pg_catalog"."default",
  "yywzc" varchar(30) COLLATE "pg_catalog"."default",
  "zcfzl" varchar(30) COLLATE "pg_catalog"."default",
  "zcjzss" varchar(30) COLLATE "pg_catalog"."default",
  "zcze" varchar(30) COLLATE "pg_catalog"."default",
  "zjgc" varchar(30) COLLATE "pg_catalog"."default",
  "zzcjll" varchar(30) COLLATE "pg_catalog"."default",
  "zzczzl" varchar(30) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."cbze" IS '成本总额';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."ch" IS '存货';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."cqdtfy" IS '长期待摊费用';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."cqgqtz" IS '长期股权投资';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."cwfy" IS '财务费用';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."cyzdqtz" IS '持有至到期投资';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."dysdszc" IS '递延所得税资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."fldzc" IS '非流动资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."fzze" IS '负债总额';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."gdzc" IS '固定资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."glfy" IS '管理费用';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."gsmgsgddjlr" IS '归属母公司股东的净利润占比';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."gyjzbdsy" IS '公允价值变动收益';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."hbzj" IS '货币资金';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."jlr" IS '净利润';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."jyxjrzc" IS '交易性金融资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."jzcsyl" IS '净资产收益率';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."kfzc" IS '开发支出';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."kgcsjrzc" IS '可供出售金融资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."ldzc" IS '流动资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."qjfy" IS '期间费用';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."qtfldzc" IS '其他非流动资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."qtldzc" IS '其他流动资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."qtysk" IS '其他应收款';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."qycs" IS '权益乘数';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."sdsfy" IS '所得税费用';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."srze" IS '收入总额';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."sy" IS '商誉';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."tzsy" IS '投资收益';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."tzxfdc" IS '投资性房地产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."wxzc" IS '无形资产';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."xsfy" IS '销售费用';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."yfzk" IS '预付账款';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."yszk" IS '应收账款';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."yycb" IS '营业成本';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."yyjlrl" IS '营业净利润率';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."yysjjfj" IS '营业税金及附加';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."yysr" IS '营业收入';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."yywsr" IS '营业外收入';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."yywzc" IS '营业外支出';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."zcfzl" IS '资产负债率';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."zcjzss" IS '资产减值损失';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."zcze" IS '资产总额';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."zjgc" IS '在建工程';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."zzcjll" IS '总资产净利率';
COMMENT ON COLUMN "public"."t_china_stock_finance_dupont"."zzczzl" IS '总资产周转率';

-- ----------------------------
-- Table structure for t_china_stock_finance_main
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_finance_main";
CREATE TABLE "public"."t_china_stock_finance_main" (
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "chzzts" varchar(30) COLLATE "pg_catalog"."default",
  "rq" date,
  "gsjlr" varchar(30) COLLATE "pg_catalog"."default",
  "gsjlrgdhbzz" varchar(30) COLLATE "pg_catalog"."default",
  "gsjlrtbzz" varchar(30) COLLATE "pg_catalog"."default",
  "jbmgsy" varchar(30) COLLATE "pg_catalog"."default",
  "jll" varchar(30) COLLATE "pg_catalog"."default",
  "jqjzcsyl" varchar(30) COLLATE "pg_catalog"."default",
  "jyxjlyysr" varchar(30) COLLATE "pg_catalog"."default",
  "kfjlr" varchar(30) COLLATE "pg_catalog"."default",
  "kfjlrgdhbzz" varchar(30) COLLATE "pg_catalog"."default",
  "kfjlrtbzz" varchar(30) COLLATE "pg_catalog"."default",
  "kfmgsy" varchar(30) COLLATE "pg_catalog"."default",
  "ldbl" varchar(30) COLLATE "pg_catalog"."default",
  "ldzczfz" varchar(30) COLLATE "pg_catalog"."default",
  "mggjj" varchar(30) COLLATE "pg_catalog"."default",
  "mgjyxjl" varchar(30) COLLATE "pg_catalog"."default",
  "mgjzc" varchar(30) COLLATE "pg_catalog"."default",
  "mgwfply" varchar(30) COLLATE "pg_catalog"."default",
  "mll" varchar(30) COLLATE "pg_catalog"."default",
  "mlr" varchar(30) COLLATE "pg_catalog"."default",
  "sdbl" varchar(30) COLLATE "pg_catalog"."default",
  "sjsl" varchar(30) COLLATE "pg_catalog"."default",
  "tbjzcsyl" varchar(30) COLLATE "pg_catalog"."default",
  "tbzzcsyl" varchar(30) COLLATE "pg_catalog"."default",
  "xsmgsy" varchar(30) COLLATE "pg_catalog"."default",
  "xsxjlyysr" varchar(30) COLLATE "pg_catalog"."default",
  "yskyysr" varchar(30) COLLATE "pg_catalog"."default",
  "yszkzzts" varchar(30) COLLATE "pg_catalog"."default",
  "yyzsr" varchar(30) COLLATE "pg_catalog"."default",
  "yyzsrgdhbzz" varchar(30) COLLATE "pg_catalog"."default",
  "yyzsrtbzz" varchar(30) COLLATE "pg_catalog"."default",
  "zcfzl" varchar(30) COLLATE "pg_catalog"."default",
  "zzczzy" varchar(30) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."chzzts" IS '存货周转天数(天)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."gsjlr" IS '归属净利润(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."gsjlrgdhbzz" IS '归属净利润滚动环比增长(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."gsjlrtbzz" IS '归属净利润同比增长(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."jbmgsy" IS '基本每股收益(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."jll" IS '净利率(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."jqjzcsyl" IS '加权净资产收益率(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."jyxjlyysr" IS '经营现金流/营业收入';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."kfjlr" IS '扣非净利润(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."kfjlrgdhbzz" IS '扣非净利润滚动环比增长(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."kfjlrtbzz" IS '扣非净利润同比增长(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."kfmgsy" IS '扣非每股收益(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."ldbl" IS '流动比率';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."ldzczfz" IS '流动负债/总负债(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."mggjj" IS '每股公积金(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."mgjyxjl" IS '每股经营现金流(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."mgjzc" IS '每股净资产(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."mgwfply" IS '每股未分配利润(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."mll" IS '毛利率(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."mlr" IS '毛利润(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."sdbl" IS '速动比率';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."sjsl" IS '实际税率(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."tbjzcsyl" IS '摊薄净资产收益率(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."tbzzcsyl" IS '摊薄总资产收益率(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."xsmgsy" IS '稀释每股收益(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."xsxjlyysr" IS '销售现金流/营业收入';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."yskyysr" IS '预收款/营业收入';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."yszkzzts" IS '应收账款周转天数(天)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."yyzsr" IS '营业总收入(元)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."yyzsrgdhbzz" IS '营业总收入滚动环比增长(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."yyzsrtbzz" IS '营业总收入同比增长(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."zcfzl" IS '资产负债率(%)';
COMMENT ON COLUMN "public"."t_china_stock_finance_main"."zzczzy" IS '总资产周转率(次)';

-- ----------------------------
-- Table structure for t_china_stock_industry_sw
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_industry_sw";
CREATE TABLE "public"."t_china_stock_industry_sw" (
  "hy_dm" varchar(30) COLLATE "pg_catalog"."default",
  "hymc" varchar(255) COLLATE "pg_catalog"."default",
  "sjhy_dm" varchar(30) COLLATE "pg_catalog"."default",
  "lvl" varchar(2) COLLATE "pg_catalog"."default",
  "index_dm" varchar(30) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_industry_sw"."hy_dm" IS '申万行业代码';
COMMENT ON COLUMN "public"."t_china_stock_industry_sw"."hymc" IS '申万行业名称';
COMMENT ON COLUMN "public"."t_china_stock_industry_sw"."sjhy_dm" IS '上级行业代码';
COMMENT ON COLUMN "public"."t_china_stock_industry_sw"."lvl" IS '层级';
COMMENT ON COLUMN "public"."t_china_stock_industry_sw"."index_dm" IS '指数代码（聚宽用的这个代码）';

-- ----------------------------
-- Table structure for t_china_stock_industry_sw_dzb
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_industry_sw_dzb";
CREATE TABLE "public"."t_china_stock_industry_sw_dzb" (
  "hy_dm" varchar(30) COLLATE "pg_catalog"."default",
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_industry_sw_dzb"."hy_dm" IS '行业代码';
COMMENT ON COLUMN "public"."t_china_stock_industry_sw_dzb"."symbol" IS '股票代码';

-- ----------------------------
-- Table structure for t_china_stock_shareholder_gdrs
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_shareholder_gdrs";
CREATE TABLE "public"."t_china_stock_shareholder_gdrs" (
  "rq" date,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "gdrs" varchar(30) COLLATE "pg_catalog"."default",
  "gdrs_jsqbh" varchar(30) COLLATE "pg_catalog"."default",
  "cmjzd" varchar(30) COLLATE "pg_catalog"."default",
  "gj" varchar(30) COLLATE "pg_catalog"."default",
  "rjcgje" varchar(30) COLLATE "pg_catalog"."default",
  "rjltg" varchar(30) COLLATE "pg_catalog"."default",
  "rjltg_jsqbh" varchar(30) COLLATE "pg_catalog"."default",
  "qsdgdcghj" varchar(30) COLLATE "pg_catalog"."default",
  "qsdltgdcghj" varchar(30) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."gdrs" IS '股东人数(户)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."gdrs_jsqbh" IS '股东人数(户)较上期变化(%)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."cmjzd" IS '筹码集中度';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."gj" IS '股价(元)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."rjcgje" IS '人均持股金额(元)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."rjltg" IS '人均流通股(股)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."rjltg_jsqbh" IS '人均流通股(股)较上期变化(%)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."qsdgdcghj" IS '前十大股东持股合计(%)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_gdrs"."qsdltgdcghj" IS '前十大流通股东持股合计(%)';

-- ----------------------------
-- Table structure for t_china_stock_shareholder_jjcg
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_shareholder_jjcg";
CREATE TABLE "public"."t_china_stock_shareholder_jjcg" (
  "rq" date,
  "jjdm" varchar(30) COLLATE "pg_catalog"."default",
  "jjmc" varchar(255) COLLATE "pg_catalog"."default",
  "cgs" varchar(100) COLLATE "pg_catalog"."default",
  "cgsz" varchar(100) COLLATE "pg_catalog"."default",
  "zzgbb" varchar(30) COLLATE "pg_catalog"."default",
  "zltb" varchar(30) COLLATE "pg_catalog"."default",
  "symbol" varchar(30) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_shareholder_jjcg"."jjdm" IS '基金代码';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_jjcg"."jjmc" IS '基金名称';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_jjcg"."cgs" IS '持股数(股)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_jjcg"."cgsz" IS '持仓市值(元)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_jjcg"."zzgbb" IS '占总股本比';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_jjcg"."zltb" IS '占流通比';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_jjcg"."symbol" IS '占净值比';

-- ----------------------------
-- Table structure for t_china_stock_shareholder_sdgd
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_shareholder_sdgd";
CREATE TABLE "public"."t_china_stock_shareholder_sdgd" (
  "rq" date,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "gdmc" varchar(300) COLLATE "pg_catalog"."default",
  "gflx" varchar(255) COLLATE "pg_catalog"."default",
  "cgs" varchar(100) COLLATE "pg_catalog"."default",
  "zltgbcgbl" varchar(30) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_shareholder_sdgd"."gdmc" IS '股东名称';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_sdgd"."gflx" IS '股份类型';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_sdgd"."cgs" IS '持股数(股)';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_sdgd"."zltgbcgbl" IS '占总股本持股比例';

-- ----------------------------
-- Table structure for t_china_stock_shareholder_sjkzr
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_shareholder_sjkzr";
CREATE TABLE "public"."t_china_stock_shareholder_sjkzr" (
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "sjkzr" varchar(350) COLLATE "pg_catalog"."default",
  "cgbl" varchar(10) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_china_stock_shareholder_sjkzr"."symbol" IS '股票代码';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_sjkzr"."sjkzr" IS '实际控制人';
COMMENT ON COLUMN "public"."t_china_stock_shareholder_sjkzr"."cgbl" IS '持股比例';

-- ----------------------------
-- Table structure for t_china_stock_trade_1990_2000
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_1990_2000";
CREATE TABLE "public"."t_china_stock_trade_1990_2000" (
  "trade_date" date,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_1990_2000"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2001_2003
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2001_2003";
CREATE TABLE "public"."t_china_stock_trade_2001_2003" (
  "trade_date" date,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2001_2003"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2004_2006
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2004_2006";
CREATE TABLE "public"."t_china_stock_trade_2004_2006" (
  "trade_date" date,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2004_2006"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2007_2009
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2007_2009";
CREATE TABLE "public"."t_china_stock_trade_2007_2009" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2007_2009"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2010
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2010";
CREATE TABLE "public"."t_china_stock_trade_2010" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2010"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2011
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2011";
CREATE TABLE "public"."t_china_stock_trade_2011" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2011"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2012
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2012";
CREATE TABLE "public"."t_china_stock_trade_2012" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2012"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2013
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2013";
CREATE TABLE "public"."t_china_stock_trade_2013" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2013"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2014
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2014";
CREATE TABLE "public"."t_china_stock_trade_2014" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2014"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2015
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2015";
CREATE TABLE "public"."t_china_stock_trade_2015" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2015"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2016
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2016";
CREATE TABLE "public"."t_china_stock_trade_2016" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2016"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2017
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2017";
CREATE TABLE "public"."t_china_stock_trade_2017" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2017"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2018
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2018";
CREATE TABLE "public"."t_china_stock_trade_2018" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2018"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2019
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2019";
CREATE TABLE "public"."t_china_stock_trade_2019" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2019"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2020
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2020";
CREATE TABLE "public"."t_china_stock_trade_2020" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2020"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_2021
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_2021";
CREATE TABLE "public"."t_china_stock_trade_2021" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_2021"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_current
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_current";
CREATE TABLE "public"."t_china_stock_trade_current" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6),
  "syldt" numeric(100,6),
  "sjl" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."circulate_market" IS '流通市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."syldt" IS '市盈率（动态）';
COMMENT ON COLUMN "public"."t_china_stock_trade_current"."sjl" IS '市净率';

-- ----------------------------
-- Table structure for t_china_stock_trade_history
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_china_stock_trade_history";
CREATE TABLE "public"."t_china_stock_trade_history" (
  "trade_date" date NOT NULL,
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "symbol_name" varchar(255) COLLATE "pg_catalog"."default",
  "open" numeric(50,6),
  "high" numeric(50,6),
  "low" numeric(50,6),
  "close" numeric(50,6),
  "volume" numeric(50,6),
  "money" numeric(50,6),
  "change_amount" numeric(50,6),
  "change_rate" numeric(50,6),
  "amplitude" numeric(50,6),
  "turnover" numeric(50,6),
  "pre_close" numeric(50,6),
  "high_limit" numeric(50,6),
  "low_limit" numeric(50,6),
  "total_market" numeric(100,6),
  "circulate_market" numeric(100,6)
)
;
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."trade_date" IS '交易日期';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."symbol" IS '交易代码';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."symbol_name" IS '交易名称';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."open" IS '开盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."high" IS '最高价';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."low" IS '最低价';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."close" IS '收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."volume" IS '成交量';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."money" IS '成交金额';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."change_amount" IS '涨跌额';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."change_rate" IS '涨跌幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."amplitude" IS '振幅';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."turnover" IS '换手率';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."pre_close" IS '前一日收盘价';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."high_limit" IS '涨停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."low_limit" IS '跌停价';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."total_market" IS '总市值';
COMMENT ON COLUMN "public"."t_china_stock_trade_history"."circulate_market" IS '流通市值';

-- ----------------------------
-- Table structure for t_dm_jqdata_market
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_dm_jqdata_market";
CREATE TABLE "public"."t_dm_jqdata_market" (
  "market_name" varchar(255) COLLATE "pg_catalog"."default",
  "market_postfix" varchar(255) COLLATE "pg_catalog"."default",
  "market_lx" varchar(255) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for t_xt_logger_mx
-- ----------------------------
DROP TABLE IF EXISTS "public"."t_xt_logger_mx";
CREATE TABLE "public"."t_xt_logger_mx" (
  "security_type" varchar(30) COLLATE "pg_catalog"."default",
  "symbol" varchar(30) COLLATE "pg_catalog"."default",
  "operation" varchar(100) COLLATE "pg_catalog"."default",
  "status" char(1) COLLATE "pg_catalog"."default",
  "business" varchar(100) COLLATE "pg_catalog"."default",
  "create_date" date,
  "batch_number" varchar(255) COLLATE "pg_catalog"."default",
  "row_number" varchar(64) COLLATE "pg_catalog"."default",
  "message" varchar(300) COLLATE "pg_catalog"."default"
)
;
COMMENT ON COLUMN "public"."t_xt_logger_mx"."security_type" IS '标类型';
COMMENT ON COLUMN "public"."t_xt_logger_mx"."symbol" IS '标代码';
COMMENT ON COLUMN "public"."t_xt_logger_mx"."operation" IS '操作类型';
COMMENT ON COLUMN "public"."t_xt_logger_mx"."status" IS '成功标志';
COMMENT ON COLUMN "public"."t_xt_logger_mx"."business" IS '业务类型';
COMMENT ON COLUMN "public"."t_xt_logger_mx"."create_date" IS '录入日期';
COMMENT ON COLUMN "public"."t_xt_logger_mx"."batch_number" IS '批次序号';
COMMENT ON COLUMN "public"."t_xt_logger_mx"."row_number" IS '记录数';
COMMENT ON COLUMN "public"."t_xt_logger_mx"."message" IS '详细信息';

-- ----------------------------
-- View structure for v_t_china_stock_trade
-- ----------------------------
DROP VIEW IF EXISTS "public"."v_t_china_stock_trade";
CREATE VIEW "public"."v_t_china_stock_trade" AS  SELECT t_china_stock_trade_2020.trade_date,
    t_china_stock_trade_2020.symbol,
    t_china_stock_trade_2020.symbol_name,
    t_china_stock_trade_2020.open,
    t_china_stock_trade_2020.high,
    t_china_stock_trade_2020.low,
    t_china_stock_trade_2020.close,
    t_china_stock_trade_2020.volume,
    t_china_stock_trade_2020.money,
    t_china_stock_trade_2020.change_amount,
    t_china_stock_trade_2020.change_rate,
    t_china_stock_trade_2020.amplitude,
    t_china_stock_trade_2020.turnover,
    t_china_stock_trade_2020.pre_close,
    t_china_stock_trade_2020.high_limit,
    t_china_stock_trade_2020.low_limit,
    t_china_stock_trade_2020.total_market,
    t_china_stock_trade_2020.circulate_market
   FROM t_china_stock_trade_2020
UNION ALL
 SELECT t_china_stock_trade_2019.trade_date,
    t_china_stock_trade_2019.symbol,
    t_china_stock_trade_2019.symbol_name,
    t_china_stock_trade_2019.open,
    t_china_stock_trade_2019.high,
    t_china_stock_trade_2019.low,
    t_china_stock_trade_2019.close,
    t_china_stock_trade_2019.volume,
    t_china_stock_trade_2019.money,
    t_china_stock_trade_2019.change_amount,
    t_china_stock_trade_2019.change_rate,
    t_china_stock_trade_2019.amplitude,
    t_china_stock_trade_2019.turnover,
    t_china_stock_trade_2019.pre_close,
    t_china_stock_trade_2019.high_limit,
    t_china_stock_trade_2019.low_limit,
    t_china_stock_trade_2019.total_market,
    t_china_stock_trade_2019.circulate_market
   FROM t_china_stock_trade_2019
UNION ALL
 SELECT t_china_stock_trade_2018.trade_date,
    t_china_stock_trade_2018.symbol,
    t_china_stock_trade_2018.symbol_name,
    t_china_stock_trade_2018.open,
    t_china_stock_trade_2018.high,
    t_china_stock_trade_2018.low,
    t_china_stock_trade_2018.close,
    t_china_stock_trade_2018.volume,
    t_china_stock_trade_2018.money,
    t_china_stock_trade_2018.change_amount,
    t_china_stock_trade_2018.change_rate,
    t_china_stock_trade_2018.amplitude,
    t_china_stock_trade_2018.turnover,
    t_china_stock_trade_2018.pre_close,
    t_china_stock_trade_2018.high_limit,
    t_china_stock_trade_2018.low_limit,
    t_china_stock_trade_2018.total_market,
    t_china_stock_trade_2018.circulate_market
   FROM t_china_stock_trade_2018
UNION ALL
 SELECT t_china_stock_trade_2017.trade_date,
    t_china_stock_trade_2017.symbol,
    t_china_stock_trade_2017.symbol_name,
    t_china_stock_trade_2017.open,
    t_china_stock_trade_2017.high,
    t_china_stock_trade_2017.low,
    t_china_stock_trade_2017.close,
    t_china_stock_trade_2017.volume,
    t_china_stock_trade_2017.money,
    t_china_stock_trade_2017.change_amount,
    t_china_stock_trade_2017.change_rate,
    t_china_stock_trade_2017.amplitude,
    t_china_stock_trade_2017.turnover,
    t_china_stock_trade_2017.pre_close,
    t_china_stock_trade_2017.high_limit,
    t_china_stock_trade_2017.low_limit,
    t_china_stock_trade_2017.total_market,
    t_china_stock_trade_2017.circulate_market
   FROM t_china_stock_trade_2017
UNION ALL
 SELECT t_china_stock_trade_2016.trade_date,
    t_china_stock_trade_2016.symbol,
    t_china_stock_trade_2016.symbol_name,
    t_china_stock_trade_2016.open,
    t_china_stock_trade_2016.high,
    t_china_stock_trade_2016.low,
    t_china_stock_trade_2016.close,
    t_china_stock_trade_2016.volume,
    t_china_stock_trade_2016.money,
    t_china_stock_trade_2016.change_amount,
    t_china_stock_trade_2016.change_rate,
    t_china_stock_trade_2016.amplitude,
    t_china_stock_trade_2016.turnover,
    t_china_stock_trade_2016.pre_close,
    t_china_stock_trade_2016.high_limit,
    t_china_stock_trade_2016.low_limit,
    t_china_stock_trade_2016.total_market,
    t_china_stock_trade_2016.circulate_market
   FROM t_china_stock_trade_2016
UNION ALL
 SELECT t_china_stock_trade_2015.trade_date,
    t_china_stock_trade_2015.symbol,
    t_china_stock_trade_2015.symbol_name,
    t_china_stock_trade_2015.open,
    t_china_stock_trade_2015.high,
    t_china_stock_trade_2015.low,
    t_china_stock_trade_2015.close,
    t_china_stock_trade_2015.volume,
    t_china_stock_trade_2015.money,
    t_china_stock_trade_2015.change_amount,
    t_china_stock_trade_2015.change_rate,
    t_china_stock_trade_2015.amplitude,
    t_china_stock_trade_2015.turnover,
    t_china_stock_trade_2015.pre_close,
    t_china_stock_trade_2015.high_limit,
    t_china_stock_trade_2015.low_limit,
    t_china_stock_trade_2015.total_market,
    t_china_stock_trade_2015.circulate_market
   FROM t_china_stock_trade_2015
UNION ALL
 SELECT t_china_stock_trade_2014.trade_date,
    t_china_stock_trade_2014.symbol,
    t_china_stock_trade_2014.symbol_name,
    t_china_stock_trade_2014.open,
    t_china_stock_trade_2014.high,
    t_china_stock_trade_2014.low,
    t_china_stock_trade_2014.close,
    t_china_stock_trade_2014.volume,
    t_china_stock_trade_2014.money,
    t_china_stock_trade_2014.change_amount,
    t_china_stock_trade_2014.change_rate,
    t_china_stock_trade_2014.amplitude,
    t_china_stock_trade_2014.turnover,
    t_china_stock_trade_2014.pre_close,
    t_china_stock_trade_2014.high_limit,
    t_china_stock_trade_2014.low_limit,
    t_china_stock_trade_2014.total_market,
    t_china_stock_trade_2014.circulate_market
   FROM t_china_stock_trade_2014
UNION ALL
 SELECT t_china_stock_trade_2013.trade_date,
    t_china_stock_trade_2013.symbol,
    t_china_stock_trade_2013.symbol_name,
    t_china_stock_trade_2013.open,
    t_china_stock_trade_2013.high,
    t_china_stock_trade_2013.low,
    t_china_stock_trade_2013.close,
    t_china_stock_trade_2013.volume,
    t_china_stock_trade_2013.money,
    t_china_stock_trade_2013.change_amount,
    t_china_stock_trade_2013.change_rate,
    t_china_stock_trade_2013.amplitude,
    t_china_stock_trade_2013.turnover,
    t_china_stock_trade_2013.pre_close,
    t_china_stock_trade_2013.high_limit,
    t_china_stock_trade_2013.low_limit,
    t_china_stock_trade_2013.total_market,
    t_china_stock_trade_2013.circulate_market
   FROM t_china_stock_trade_2013
UNION ALL
 SELECT t_china_stock_trade_2012.trade_date,
    t_china_stock_trade_2012.symbol,
    t_china_stock_trade_2012.symbol_name,
    t_china_stock_trade_2012.open,
    t_china_stock_trade_2012.high,
    t_china_stock_trade_2012.low,
    t_china_stock_trade_2012.close,
    t_china_stock_trade_2012.volume,
    t_china_stock_trade_2012.money,
    t_china_stock_trade_2012.change_amount,
    t_china_stock_trade_2012.change_rate,
    t_china_stock_trade_2012.amplitude,
    t_china_stock_trade_2012.turnover,
    t_china_stock_trade_2012.pre_close,
    t_china_stock_trade_2012.high_limit,
    t_china_stock_trade_2012.low_limit,
    t_china_stock_trade_2012.total_market,
    t_china_stock_trade_2012.circulate_market
   FROM t_china_stock_trade_2012
UNION ALL
 SELECT t_china_stock_trade_2011.trade_date,
    t_china_stock_trade_2011.symbol,
    t_china_stock_trade_2011.symbol_name,
    t_china_stock_trade_2011.open,
    t_china_stock_trade_2011.high,
    t_china_stock_trade_2011.low,
    t_china_stock_trade_2011.close,
    t_china_stock_trade_2011.volume,
    t_china_stock_trade_2011.money,
    t_china_stock_trade_2011.change_amount,
    t_china_stock_trade_2011.change_rate,
    t_china_stock_trade_2011.amplitude,
    t_china_stock_trade_2011.turnover,
    t_china_stock_trade_2011.pre_close,
    t_china_stock_trade_2011.high_limit,
    t_china_stock_trade_2011.low_limit,
    t_china_stock_trade_2011.total_market,
    t_china_stock_trade_2011.circulate_market
   FROM t_china_stock_trade_2011
UNION ALL
 SELECT t_china_stock_trade_2010.trade_date,
    t_china_stock_trade_2010.symbol,
    t_china_stock_trade_2010.symbol_name,
    t_china_stock_trade_2010.open,
    t_china_stock_trade_2010.high,
    t_china_stock_trade_2010.low,
    t_china_stock_trade_2010.close,
    t_china_stock_trade_2010.volume,
    t_china_stock_trade_2010.money,
    t_china_stock_trade_2010.change_amount,
    t_china_stock_trade_2010.change_rate,
    t_china_stock_trade_2010.amplitude,
    t_china_stock_trade_2010.turnover,
    t_china_stock_trade_2010.pre_close,
    t_china_stock_trade_2010.high_limit,
    t_china_stock_trade_2010.low_limit,
    t_china_stock_trade_2010.total_market,
    t_china_stock_trade_2010.circulate_market
   FROM t_china_stock_trade_2010
UNION ALL
 SELECT t_china_stock_trade_2007_2009.trade_date,
    t_china_stock_trade_2007_2009.symbol,
    t_china_stock_trade_2007_2009.symbol_name,
    t_china_stock_trade_2007_2009.open,
    t_china_stock_trade_2007_2009.high,
    t_china_stock_trade_2007_2009.low,
    t_china_stock_trade_2007_2009.close,
    t_china_stock_trade_2007_2009.volume,
    t_china_stock_trade_2007_2009.money,
    t_china_stock_trade_2007_2009.change_amount,
    t_china_stock_trade_2007_2009.change_rate,
    t_china_stock_trade_2007_2009.amplitude,
    t_china_stock_trade_2007_2009.turnover,
    t_china_stock_trade_2007_2009.pre_close,
    t_china_stock_trade_2007_2009.high_limit,
    t_china_stock_trade_2007_2009.low_limit,
    t_china_stock_trade_2007_2009.total_market,
    t_china_stock_trade_2007_2009.circulate_market
   FROM t_china_stock_trade_2007_2009
UNION ALL
 SELECT t_china_stock_trade_2004_2006.trade_date,
    t_china_stock_trade_2004_2006.symbol,
    t_china_stock_trade_2004_2006.symbol_name,
    t_china_stock_trade_2004_2006.open,
    t_china_stock_trade_2004_2006.high,
    t_china_stock_trade_2004_2006.low,
    t_china_stock_trade_2004_2006.close,
    t_china_stock_trade_2004_2006.volume,
    t_china_stock_trade_2004_2006.money,
    t_china_stock_trade_2004_2006.change_amount,
    t_china_stock_trade_2004_2006.change_rate,
    t_china_stock_trade_2004_2006.amplitude,
    t_china_stock_trade_2004_2006.turnover,
    t_china_stock_trade_2004_2006.pre_close,
    t_china_stock_trade_2004_2006.high_limit,
    t_china_stock_trade_2004_2006.low_limit,
    t_china_stock_trade_2004_2006.total_market,
    t_china_stock_trade_2004_2006.circulate_market
   FROM t_china_stock_trade_2004_2006
UNION ALL
 SELECT t_china_stock_trade_2001_2003.trade_date,
    t_china_stock_trade_2001_2003.symbol,
    t_china_stock_trade_2001_2003.symbol_name,
    t_china_stock_trade_2001_2003.open,
    t_china_stock_trade_2001_2003.high,
    t_china_stock_trade_2001_2003.low,
    t_china_stock_trade_2001_2003.close,
    t_china_stock_trade_2001_2003.volume,
    t_china_stock_trade_2001_2003.money,
    t_china_stock_trade_2001_2003.change_amount,
    t_china_stock_trade_2001_2003.change_rate,
    t_china_stock_trade_2001_2003.amplitude,
    t_china_stock_trade_2001_2003.turnover,
    t_china_stock_trade_2001_2003.pre_close,
    t_china_stock_trade_2001_2003.high_limit,
    t_china_stock_trade_2001_2003.low_limit,
    t_china_stock_trade_2001_2003.total_market,
    t_china_stock_trade_2001_2003.circulate_market
   FROM t_china_stock_trade_2001_2003
UNION ALL
 SELECT t_china_stock_trade_1990_2000.trade_date,
    t_china_stock_trade_1990_2000.symbol,
    t_china_stock_trade_1990_2000.symbol_name,
    t_china_stock_trade_1990_2000.open,
    t_china_stock_trade_1990_2000.high,
    t_china_stock_trade_1990_2000.low,
    t_china_stock_trade_1990_2000.close,
    t_china_stock_trade_1990_2000.volume,
    t_china_stock_trade_1990_2000.money,
    t_china_stock_trade_1990_2000.change_amount,
    t_china_stock_trade_1990_2000.change_rate,
    t_china_stock_trade_1990_2000.amplitude,
    t_china_stock_trade_1990_2000.turnover,
    t_china_stock_trade_1990_2000.pre_close,
    t_china_stock_trade_1990_2000.high_limit,
    t_china_stock_trade_1990_2000.low_limit,
    t_china_stock_trade_1990_2000.total_market,
    t_china_stock_trade_1990_2000.circulate_market
   FROM t_china_stock_trade_1990_2000;

-- ----------------------------
-- Primary Key structure for table t_china_index_1990_2010
-- ----------------------------
ALTER TABLE "public"."t_china_index_1990_2010" ADD CONSTRAINT "pk" PRIMARY KEY ("idd");

-- ----------------------------
-- Indexes structure for table t_china_stock_area_eastmoney_dzb
-- ----------------------------
CREATE INDEX "idx_ t_china_stock_concept_eastmoney_dzb_copy1" ON "public"."t_china_stock_area_eastmoney_dzb" USING btree (
  "area_dm" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_concept_eastmoney_dzb
-- ----------------------------
CREATE INDEX "idx_ t_china_stock_concept_eastmoney_dzb" ON "public"."t_china_stock_concept_eastmoney_dzb" USING btree (
  "concept_dm" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_finance_dupont
-- ----------------------------
CREATE INDEX "idx_t_china_stock_finance_dupont" ON "public"."t_china_stock_finance_dupont" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_finance_main
-- ----------------------------
CREATE INDEX "idx_t_china_stock_finance_main" ON "public"."t_china_stock_finance_main" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_shareholder_gdrs
-- ----------------------------
CREATE INDEX "idx_t_china_stock_shareholder_gdrs_symbol" ON "public"."t_china_stock_shareholder_gdrs" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_shareholder_jjcg
-- ----------------------------
CREATE INDEX "idx_t_china_stock_shareholder_jjcg_symbol" ON "public"."t_china_stock_shareholder_jjcg" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_shareholder_sdgd
-- ----------------------------
CREATE INDEX "idx_t_china_stock_shareholder_sdgd_symbol" ON "public"."t_china_stock_shareholder_sdgd" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_shareholder_sjkzr
-- ----------------------------
CREATE INDEX "idx_t_china_stock_shareholder_sjkzr_symbol" ON "public"."t_china_stock_shareholder_sjkzr" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_1990_2000
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_1990_2004_date_copy1" ON "public"."t_china_stock_trade_1990_2000" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_1990_2004_symbol_copy1" ON "public"."t_china_stock_trade_1990_2000" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2001_2003
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_1990_2004_date_copy1_copy1" ON "public"."t_china_stock_trade_2001_2003" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_1990_2004_symbol_copy1_copy1" ON "public"."t_china_stock_trade_2001_2003" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2004_2006
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_1990_2004_date_copy2" ON "public"."t_china_stock_trade_2004_2006" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_1990_2004_symbol_copy2" ON "public"."t_china_stock_trade_2004_2006" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2007_2009
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2005_2009_date_copy1" ON "public"."t_china_stock_trade_2007_2009" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2005_2009_symbol_copy1" ON "public"."t_china_stock_trade_2007_2009" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2010
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2010_date" ON "public"."t_china_stock_trade_2010" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2010_symbol" ON "public"."t_china_stock_trade_2010" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2011
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2011_date" ON "public"."t_china_stock_trade_2011" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2011_symbol" ON "public"."t_china_stock_trade_2011" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2012
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2012_date" ON "public"."t_china_stock_trade_2012" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2012_symbol" ON "public"."t_china_stock_trade_2012" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2013
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2013_date" ON "public"."t_china_stock_trade_2013" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2013_symbol" ON "public"."t_china_stock_trade_2013" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2014
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2014_date" ON "public"."t_china_stock_trade_2014" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2014_symbol" ON "public"."t_china_stock_trade_2014" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2015
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2015_date" ON "public"."t_china_stock_trade_2015" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2015_symbol" ON "public"."t_china_stock_trade_2015" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2016
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2016_date" ON "public"."t_china_stock_trade_2016" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2016_symbol" ON "public"."t_china_stock_trade_2016" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2017
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2017_date" ON "public"."t_china_stock_trade_2017" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2017_symbol" ON "public"."t_china_stock_trade_2017" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2018
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2018_date" ON "public"."t_china_stock_trade_2018" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2018_symbol" ON "public"."t_china_stock_trade_2018" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2019
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2019_date" ON "public"."t_china_stock_trade_2019" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2019_symbol" ON "public"."t_china_stock_trade_2019" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2020
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2020_date" ON "public"."t_china_stock_trade_2020" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2020_symbol" ON "public"."t_china_stock_trade_2020" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);

-- ----------------------------
-- Indexes structure for table t_china_stock_trade_2021
-- ----------------------------
CREATE INDEX "idx_t_china_stock_trade_2020_date_copy1" ON "public"."t_china_stock_trade_2021" USING btree (
  "trade_date" "pg_catalog"."date_ops" ASC NULLS LAST
);
CREATE INDEX "idx_t_china_stock_trade_2020_symbol_copy1" ON "public"."t_china_stock_trade_2021" USING btree (
  "symbol" COLLATE "pg_catalog"."default" "pg_catalog"."text_ops" ASC NULLS LAST
);
